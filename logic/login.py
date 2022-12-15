import requests

token_id = ''

def logged(email,password):
    if(email == ''):
        email = 'none'
    if(password == ''):
        password = 'none'
    url = 'https://api-uat-001.ormuco.com:5000/v3/auth/tokens'
    payload = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": email,
                    "domain": {
                        "name": "default"
                    },
                    "password": password
                }
            }
        }
    }
    }
    res = requests.post(url = url,json = payload)
    if(res.json().get('token')):
        token_id = res.json().get('token').get('id')
        return token_id
    else:
     return False
    
