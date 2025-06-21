"""Loading the data from Titanic CSV into a SQLite database."""

import sqlite3
import pandas as pd


def load_csv(filepath):
    """Load data from CSV to a DataFrame."""
    return pd.read_csv(filepath)


def save_sqlite(dataframe, db_name, table_name):
    """Save DataFrame to a SQLite3 database."""
    conn = sqlite3.connect(db_name)
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


if __name__ == "__main__":
    # Load from CSV
    titanic_df = load_csv('data/titanic.csv')

    # Save the DataFrame to DB
    save_sqlite(titanic_df, 'titanic.db', 'titanic_data')

    print("Data loaded and saved.")
