import requests
import os
import urllib
import json

bearer_token = os.environ.get("BEARER_TOKEN")
headers = {"Authorization": f"Bearer {bearer_token}"}
hash_tag = urllib.parse.quote('#ケバブ')
url = f'https://api.twitter.com/2/tweets/search/recent?query={hash_tag} -is:retweet'
response = requests.get(url, headers=headers)
json_responce = response.json()
print(json.dumps(json_responce, indent=2, ensure_ascii=False))
