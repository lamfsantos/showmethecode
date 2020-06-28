import sqlite3
from sqlite3 import Error

database = r"pythonsqlite.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def find_all():
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT descricao, minutos FROM planos")

    rows = cur.fetchall()

    conn.close()

    return rows

def find_by_minutos(minutos):
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT descricao, minutos FROM planos WHERE minutos = ?", (minutos, ))

    rows = cur.fetchall()

    conn.close()

    return rows
