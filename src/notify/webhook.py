import urllib.request
import json

def send_webhook(url: str, message: str):
    data = json.dumps({'text': message}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req, timeout=5)
