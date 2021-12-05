import yaml
import sys

try:
    with open('/workspaces/py_twitter/src/py_yaml/config.yaml') as file:
        obj = yaml.safe_load(file)
        print("user_id {}".format(obj['user_id']))
        print("search_word {}".format(obj['search_word']))
        # print("query_params['tweet']['fields'] {}".format(obj['query_params']['tweet']['fields']))
        tweet_fields = ",".join(obj['query_params']['tweet']['fields'])
        print("tweet.fields {}".format(tweet_fields))
        # print("query_params['user']['fields'] {}".format(obj['query_params']['user']['fields']))
        user_fields = ",".join(obj['query_params']['user']['fields'])
        print("user.fields {}".format(user_fields))
        print("query_params['max_results'] {}".format(obj['query_params']['max_results']))
except Exception as e:
    print('Exception occurred while loading YAML...', file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)