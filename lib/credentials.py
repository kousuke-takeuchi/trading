import os
import json

def load_credentials(filename='credentials.json'):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'r') as f:
        credentials = json.loads(f.read())
    return credentials
