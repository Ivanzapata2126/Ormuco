import requests

def getImages(token):
    urlImage = 'https://api-uat-001.ormuco.com:9292/v2/images'
    headers = {"X-Auth-Token": token}
    response = requests.get(urlImage, headers=headers).json()
    return response.get('images')


def findId(name,data):
    for dato in data:
        if name in dato['name']:
            return dato['id']
    return None


def findVersion(name,version,data):
    for dato in data:
        if name in dato['name']:
            if(dato.get("os_version",False) and version == dato.get("os_version")):
                return dato['id']
    return None            