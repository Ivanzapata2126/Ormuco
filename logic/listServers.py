import requests
import logic.login as login
def getServers(token):
    url = "https://api-uat-001.ormuco.com:8774/v2.1/servers/detail"
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers)
    return response.json().get('servers')

def findId(name,data):
    for dato in data:
        if name in dato['name']:
            return dato['id']
    return None