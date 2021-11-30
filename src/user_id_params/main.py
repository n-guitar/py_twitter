import requests
import os
import urllib
import json

bearer_token = os.environ.get("BEARER_TOKEN")
print(bearer_token)
headers = {"Authorization": f"Bearer {bearer_token}"}
user_id = "1441015667587567626"
start_date = '2021-10-01T00:00:00.000Z'
end_date = '2021-11-01T00:00:00.000Z'
query_params = {
    'start_time': start_date,
    'end_time': end_date,
    'tweet.fields': 'author_id,text,source,created_at',
    'user.fields': 'id,name,username',
    'max_results': 100
}
url = f'https://api.twitter.com/2/users/{user_id}/tweets'
response = requests.get(url, headers=headers, params=query_params)
json_responce = response.json()
print(json.dumps(json_responce, indent=2, ensure_ascii=False))
