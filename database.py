import sqlite3

def get_db_connection():
    conn = sqlite3.connect('bank_management.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            address TEXT,
            phone TEXT UNIQUE,
            adhaar_no TEXT UNIQUE,
            pin TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Database setup complete.")
