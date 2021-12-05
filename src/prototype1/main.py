import json
import yaml
import sys

# my package
from api.pytw_api import TwitterApiClient
from db.tw_db import TwitterDBClient

# ToDo複数のuser_idをconfigにlistでセットし、dbに保存できるようにする
def get_tw_data():

    # yamlにセットした値を利用
    try:
        with open('/workspaces/py_twitter/src/prototype1/config.yaml') as file:
            obj = yaml.safe_load(file)
            user_id = obj['user_id']
            tweet_fields = ",".join(obj['query_params']['tweet']['fields'])
            user_fields = ",".join(obj['query_params']['user']['fields'])
            max_results = obj['query_params']['max_results']
    except Exception as e:
        print('Exception occurred while loading YAML...', file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)


    tw_client = TwitterApiClient()
    # user_id = "114446939"
    start_date, end_date = tw_client.get_date(10)
    query_params = {
        'start_time': start_date,
        'end_time': end_date,
        'tweet.fields': tweet_fields,
        'user.fields': user_fields,
        'max_results': max_results
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
