import os
import urllib
import json
import datetime

import requests

class TwitterApiClient(object):
    def __init__(self, base_url=None) -> None:
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = 'https://api.twitter.com/2'
        bearer_token = os.environ.get("BEARER_TOKEN")
        if not bearer_token:
            raise Exception('Please set your API token to BEARER_TOKEN')
        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + bearer_token
        }

    def call_api(self, url, method='get', params=None):
        req_method = getattr(requests, method)
        try:
            res = req_method(self.base_url+url,
                             headers=self.headers,
                             params=params)
            return res.json()
        except Exception as e:
            raise Exception('Failed to call API: %s' % str(e))


    def get_user_tweets(self, user_id, params):
        url = f'/users/{user_id}/tweets'
        return self.call_api(url=url, params=params)

def get_date(day_ago):
    dt = datetime.date.today()
    the_day_before = dt + datetime.timedelta(days=-day_ago)
    start_date = the_day_before.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    end_date = dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return start_date, end_date


if __name__ == '__main__':
    tw_client = TwitterApiClient()

    user_id = "114446939"
    start_date, end_date = get_date(2)
    # print(f'start_date:{start_date} end_date:{end_date}')
    # start_date = '2021-12-03T00:00:00.000Z'
    # end_date = '2021-12-05T00:00:00.000Z'
    query_params = {
        'start_time': start_date,
        'end_time': end_date,
        'tweet.fields': 'author_id,text,source,created_at',
        'user.fields': 'id,name,username',
        'max_results': 100
    }
    json_responce = tw_client.get_user_tweets(user_id=user_id, params=query_params)
    print(json.dumps(json_responce, indent=2, ensure_ascii=False))
