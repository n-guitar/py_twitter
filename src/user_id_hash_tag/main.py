import requests
import os
import urllib
import json

bearer_token = os.environ.get("BEARER_TOKEN")
headers = {"Authorization": f"Bearer {bearer_token}"}
user_id = input('Enter your user_id: ')
url = f'https://api.twitter.com/2/users/{user_id}/tweets'
response = requests.get(url, headers=headers)
json_responce = response.json()

input_hash_tag = input('Enter your hash_tag: ')
hash_tag = '#' + input_hash_tag

for data in json_responce['data']:
    if hash_tag in data['text']:
        print(json.dumps(data, indent=2, ensure_ascii=False))
