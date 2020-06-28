import sqlite3
#mport os
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

    cur = conn.cursor()
    cur.execute("SELECT DISTINCT origem FROM tarifas")

    rows = cur.fetchall()
    listString = []

    for row in rows:
        listString.append(''.join(row))

    conn.close()

    return listString

def find_valor(ddd_origem, ddd_destino):
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT valor FROM tarifas WHERE origem = ? AND destino = ?", (ddd_origem, ddd_destino))

    rows = cur.fetchall()

    if(len(rows)>0):
        stringFloat = "".join(str(rows[0]))
        stringFloatFormated = stringFloat.replace('(','').replace(')', '').replace(',', '')
        valor = float(stringFloatFormated)

        conn.close()

        return valor

    return rows
