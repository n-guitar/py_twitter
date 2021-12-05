import sqlite3

# dbをなければ作成&接続し、connectionオブジェクトを返す
def get_db():
    db = 'twdb.db'
    conn = sqlite3.connect(db)
    init_table(conn)
    return conn

# create table
def init_table(conn):
    cur = conn.cursor()
    # tableがなければ作成
    cur.execute(
        'CREATE TABLE IF NOT EXISTS t_twdata(id INTEGER PRIMARY KEY AUTOINCREMENT,author_id TEXT, text TEXT, source TEXT, created_at TEXT )'
        )

if __name__ == '__main__':
    conn = get_db()
    conn.close()