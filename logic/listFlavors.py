import requests

def getFlavors(token):
    url = 'https://api-uat-001.ormuco.com:8774/v2.1/flavors/detail'
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers).json()
    return response.get('flavors')