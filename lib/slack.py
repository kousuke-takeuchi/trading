import json
import requests

from credentials import load_credentials


def post_slack(message):
    credentials = load_credentials()
    url = credentials.get('SLACK_WEBHOOK_URL')
    payload = {
        'channel': '#report',
        'username': 'AdRobot',
        'text': message,
        'icon_emoji': ':robot_face:'
    }
    requests.post(url, data=json.dumps(payload))
