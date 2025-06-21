"""Loading the data from titantic"""

import pandas as pd
import sqlite3

def load_csv(filepath):
    """Load data from CSV to DF"""
    return pd.read_csv(filepath)

def save_sqlite(df, db_name, table_name):
    """Save DF to sqlite DB"""
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    # Load  from CSV
    df = load_csv('titanic.csv')
    
    # Save the df to DB
    save_sqlite(df, 'titanic.db', 'titanic_data')
    
    print("Data loaded and saved.")
