import json
from base64 import b32encode, b32decode

from keygen import keygen


def get_keys(username):
    keyfile = username + "_keys.json"
    try:
        with open(keyfile) as f:
            data = json.load(f)
            keyword_key = b32decode(data['keyword_key'])
            file_key = b32decode(data['file_key'])
            user_exists = True
    except IOError:
        keyword_key, file_key = keygen()
        keys_dict = {
            'keyword_key': b32encode(keyword_key).decode('utf-8'),
            'file_key': b32encode(file_key).decode('utf-8')
        }
        with open(keyfile, 'w+') as fp:
            json.dump(keys_dict, fp)
        user_exists = False
    return keyword_key, file_key, user_exists
