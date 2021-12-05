import sqlite3

class TwitterDBClient(object):
    def __init__(self, database=None):
        if database:
            self.database = database
        else:
            self.database = '/workspaces/py_twitter/twdb.db'

# dbをなければ作成&接続し、connectionオブジェクトを返す
    def create_or_get_db(self):
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        # tableがなければ作成
        cur.execute(
            'CREATE TABLE IF NOT EXISTS t_twdata(tw_id INTEGER PRIMARY KEY, author_id TEXT, text TEXT, source TEXT, created_at TEXT )'
            )
        return conn

    def insert_table(self, conn, insert_data):
        cur = conn.cursor()
        sql = 'insert into t_twdata (tw_id, author_id, text, source, created_at) values (?,?,?,?,?)'
        # Todo 同じkeyのときのエラー処理
        cur.executemany(sql, insert_data)
        conn.commit()

if __name__ == '__main__':
    data = [{'text': 'RT @AriyoshiQuiz: ＃有吉クイズ\n＃野村アナ が写真展リポート❗️\n素敵な写真に感激してます\n\n★渋谷パルコでは、\n12月6日（月）まで開催中です\n\n★大阪・心斎橋パルコでは、\n12月10日（金）〜19日（日）\nカレンダーとグッズのポップアップショップを開催。…', 'created_at': '2021-12-03T07:56:24.000Z', 'id': '1466677686596947968', 'author_id': '114446939', 'source': 'Twitter for iPhone'}, {'text': '了解しました https://t.co/ub9XY5So37', 'created_at': '2021-12-03T07:31:34.000Z', 'id': '1466671437042036740', 'author_id': '114446939', 'source': 'Twitter for iPhone'}, {'text': 'RT @karisome_EX: 今日3日(金)よる8時からは\n#かりそめ天国\n\nマツコさん有吉さんが、\n「自分流の地方の楽しみ方」を\n語ります。\n\nマツコさん\n「デパートでその街の全容が分かるんだよね」\n\n有吉さんが\nガイドブックでドキドキする\nポイントとは…？\n\nお楽しみに…', 'created_at': '2021-12-03T04:33:02.000Z', 'id': '1466626508223840258', 'author_id': '114446939', 'source': 'Twitter for iPhone'}]
    sorted_data = [sorted(d.keys()) for d in data]
    insert_data = [tuple(d.values()) for d in data]

    db_client = TwitterDBClient()
    conn = db_client.create_or_get_db()
    db_client.insert_table(conn=conn, insert_data=insert_data)
    print("end")

    conn.close()
