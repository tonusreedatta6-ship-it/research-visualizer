import sqlite3

def connect():
    return sqlite3.connect("data/research.db")


def create_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            field TEXT,
            author TEXT,
            university TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_data(title, field, author, university):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO papers (title, field, author, university)
        VALUES (?, ?, ?, ?)
    """, (title, field, author, university))

    conn.commit()
    conn.close()


def get_data_by_university(university):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT field, COUNT(*)
        FROM papers
        WHERE LOWER(university) = LOWER(?)
        GROUP BY field
    """, (university,))

    data = cursor.fetchall()
    conn.close()

    return dict(data)