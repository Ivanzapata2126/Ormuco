import requests

def getNetworks(token):
    url = 'https://api-uat-001.ormuco.com:9696/v2.0/networks'
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers).json()
    return response.get('networks')