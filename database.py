import sqlite3
from datetime import timedelta
from datetime import date

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
            date TEXT NOT NULL UNIQUE,
            workday INTEGER NOT NULL,
            present INTEGER NOT NULL
        )
        ''')
        con.commit()

def insert_values(cur_date, workday, presence):
    try: 
        with connect_db() as con:
            cur = con.cursor()
            cur.execute('''
            INSERT INTO attendance (date, workday, present) VALUES
            (?, ?, ?)
            ''', (cur_date, workday, presence)) 
            con.commit()
            return True
    except:
        print(f"Error while adding data")
        return False

def fill_missing_dates(last_date, cur_date):
    with connect_db() as con:
        cur = con.cursor()
        while last_date < cur_date - timedelta(days=1):
            last_date += timedelta(days=1)
            weekday = last_date.weekday()
            workday = weekday < 5
            if workday:
                workday = 1
                presence = 0
            else:
                workday = 0
                presence = 3
            cur.execute('''
                INSERT INTO attendance (date, workday, present) VALUES
                (?, ?, ?)
            ''', (last_date, workday, presence))

def update_dates(cur_date):
    with connect_db() as con:
        cur = con.cursor()
        cur.execute('''
        SELECT MAX(date)
        FROM attendance;
        ''')
        last_entry = cur.fetchone()
        last_date_str = last_entry[0]
        if last_date_str == None:
            return
        last_date = date.strptime(last_date_str, "%Y-%m-%d")
        if last_date < cur_date - timedelta(days=1):
            fill_missing_dates(last_date, cur_date)
