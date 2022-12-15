import requests


def getFloating(token):
    url = 'https://api-uat-001.ormuco.com:9696/v2.0/floatingips'
    headers = {"X-Auth-Token": token}
    response = requests.get(url=url,headers=headers).json()
    return response.get('floatingips')


def assignFloating(token,serverId,ipFixedId):
    url = f'https://api-uat-001.ormuco.com:8774/v2.1/servers/{serverId}/ips'
    urlAssign = f'https://api-uat-001.ormuco.com:8774/v2.1/servers/{serverId}/action'
    headers = {"X-Auth-Token": token}
    response = requests.get(url=url,headers=headers).json()
    response = response.get('addresses').get('default-network')
    ip = response[0]['addr']
    data = {
    "addFloatingIp" : {
        "address": ipFixedId,
        "fixed_address": ip
    }
    }
    responseFloating = requests.post(url = urlAssign,headers=headers,json = data)
    return (responseFloating.status_code)
