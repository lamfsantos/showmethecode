import sqlite3
import os
from sqlite3 import Error

# path = os.path.dirname(os.path.abspath(__file__))
# db = os.path.join(path, )
database = r"pythonsqlite.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def find_all_ddds():
    conn = create_connection(database)

    print(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT origem FROM tarifas")

    rows = cur.fetchall()
    listString = []

    for row in rows:
        listString.append(''.join(row))

    conn.close()

    return listString
