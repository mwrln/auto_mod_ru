import json
import string 


def preprocess(text):
    return ''.join(c if c not in string.punctuation else f' {c} ' for c in text.lower() )


def get_config(path):
    with open(path, 'r') as f:
        return json.load(f)
