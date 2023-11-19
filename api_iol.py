'''api requests'''
import requests
import urls

def req_token(user, password):
    """request token iol"""
    data = {
        "username": user,
        "password": password,
        "grant_type": "password",
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    ret = requests.post(url=urls.token, data=data, headers=headers, timeout=10)
    return ret
def ref_token(refresh_token):
    '''Refresh token iol'''
    data = {
        "refresh_token": refresh_token,
        "grant_type": 'refresh_token',
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    ret = requests.post(url=urls.token, data=data, headers=headers, timeout=10)
    return ret
