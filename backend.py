import sqlite3

def connect():
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS record (id INTEGER PRIMARY KEY, name text, instrument integer, date integer, remarks text)")
    conn.commit()
    conn.close()

def insert(name,instrument,date,remarks):
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO record VALUES (NULL,?,?,?,?)",(name,instrument,date,remarks))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM record")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",instrument="",date="",remarks=""):
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM record WHERE name=? OR instrument=? OR date=? OR remarks=?", (name,instrument,date,remarks))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM record WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,instrument,date,remark):
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("update record SET name=?, instrument=?, date=?, remarks=? WHERE id=?",(name,instrument,date,remark,id))
    conn.commit()
    conn.close()


connect()
