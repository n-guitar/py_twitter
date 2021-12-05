import json

# my package
from api.pytw_api import TwitterApiClient
from db.tw_db import TwitterDBClient

def get_tw_data():
    tw_client = TwitterApiClient()

    user_id = "114446939"
    start_date, end_date = tw_client.get_date(10)
    query_params = {
        'start_time': start_date,
        'end_time': end_date,
        'tweet.fields': 'author_id,text,source,created_at',
        'user.fields': 'id,name,username',
        'max_results': 100
    }
    json_responce = tw_client.get_user_tweets(user_id=user_id, params=query_params)

    if 'data' in json_responce:
        return json_responce
    else:
        return {"data": "null"}

def tuple_sorte(sort_data):
    sorted_data = (sort_data['id'],sort_data['author_id'],sort_data['text'],sort_data['source'],sort_data['created_at'])
    return sorted_data

if __name__ == '__main__':
    twdata = get_tw_data()
    # db insertのときにtupleは必ず同じ順番になるようにsortする
    sorted_data = [tuple_sorte(d) for d in twdata['data']]

    # ToDotextの検索を、sqlで行うか、twdataのところで行うか検討
    db_client = TwitterDBClient()
    conn = db_client.create_or_get_db()
    db_client.insert_table(conn=conn, insert_data=sorted_data)

    conn.close()
