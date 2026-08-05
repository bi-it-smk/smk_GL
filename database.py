import sqlite3

DATABASE = "data/attendance.db"

def connect_db():
    try:
        return sqlite3.connect(DATABASE)

    except sqlite3.OperationalError as e: 
        print(f"Connection to database failed:", e)

def create_table():
    with connect_db() as con:
        cur = con.cursor() 
        cur.execute('''
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            present INTEGER NOT NULL
        )
        ''')
        con.commit()

def insert_values(cur_date, presence):
    with connect_db() as con:
        cur = con.cursor()
        cur.execute('''
        INSERT INTO attendance (date, present) VALUES
        (?, ?)
        ''', (cur_date, presence)) 
        con.commit()