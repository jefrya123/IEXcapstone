"""Flask API for interacting with Titanic passenger data."""

import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

DATABASE = "titanic.db"


def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows row access by column name
    return conn


@app.route("/passengers", methods=["GET"])
def get_passengers():
    """Retrieve all passengers from the database."""
    conn = get_db_connection()
    passengers = conn.execute("SELECT * FROM titanic_data").fetchall()
    conn.close()
    return jsonify([dict(row) for row in passengers])


@app.route("/passengers", methods=["POST"])
def add_passenger():
    """Add a new passenger to the database."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO titanic_data (
            PassengerId, Survived, Pclass, Name, Sex, Age,
            SibSp, Parch, Ticket, Fare, Cabin, Embarked
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data.get("PassengerId"),
            data.get("Survived"),
            data.get("Pclass"),
            data.get("Name"),
            data.get("Sex"),
            data.get("Age"),
            data.get("SibSp"),
            data.get("Parch"),
            data.get("Ticket"),
            data.get("Fare"),
            data.get("Cabin"),
            data.get("Embarked"),
        ),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Passenger added successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
