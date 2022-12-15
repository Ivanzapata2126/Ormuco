import requests

def createServer(token,name,imageId,flavorId,networkId):
    urlInstance = "https://api-uat-001.ormuco.com:8774/v2.1/servers"
    headers = {"X-Auth-Token": token}
    data = {
        "server": {
            "name": name,
            "imageRef": imageId,
            "flavorRef": flavorId,
            "networks": [{"uuid": networkId}],
            "min_count": 1,
            "max_count": 1,
            "config_drive": True,
            "block_device_mapping_v2": [
                {"uuid": imageId, "source_type": "image", "boot_index": 0,
                 "delete_on_termination": True}],
            "metadata": {"source_image": imageId}
        }
    }
    response = requests.post(url=urlInstance, headers=headers, json=data)
    print(response.json())