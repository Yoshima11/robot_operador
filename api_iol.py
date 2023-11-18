'''json'''
import json
import requests
import urls

def connect_iol(user, password):
    """Pide el token a iol"""
    try:
        data = {
            "username": user,
            "password": password,
            "grant_type": "password",
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        ret = requests.post(url=urls.token, data=data, headers=headers, timeout=10)
        return json.loads(ret.text)
    except:
        print(ret.text)
