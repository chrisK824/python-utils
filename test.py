#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuthpython
import json
import argparse
import os.path


base_url = "https://staging.ubiworx.com/v2/"

# green
# gw_uuid="e76fbb02-f7d1-4e2e-8765-a48fcfd2b7f6"

# blue
# gw_uuid="e95ae983-c61c-4d36-88cc-c44c3fe4abe8" 

# orange
# gw_uuid="2940c553-b4bd-413d-a90f-dc544cfbcdeb"

# yellow
gw_uuid = "c0f796a5-c993-4f1c-a360-f3c162934c8d"

user = "test@ubiworx.com"
password = "%DzR#jolL5@Exo0c"

def main():
    response = requests.get(f'{base_url}schedules?gateway={gw_uuid}', auth=HTTPBasicAuth(user, password))
    json_results = json.loads(response.text)
    print(json_results)
    uuids = [sensor['id'] for sensor in json_results['result']]
    print(len(uuids))
    for uuid in uuids:
        result=requests.delete(f'{base_url}schedules/{uuid}', auth=HTTPBasicAuth(user, password))
        print(result.status_code)
    
    # response = requests.get(f'{base_url}sensors?gateway={gw_uuid}&perPage=500', auth=HTTPBasicAuth(user, password))
    # json_results = json.loads(response.text)
    # uuids = [sensor['id'] for sensor in json_results['result']]
    # print(len(uuids))
    # for uuid in uuids:
    #     result=requests.delete(f'{base_url}sensors/{uuid}', auth=HTTPBasicAuth(user, password))
    #     print(result.status_code)

    # response = requests.get(f'{base_url}nodes?gateway={gw_uuid}', auth=HTTPBasicAuth(user, password))
    # json_results = json.loads(response.text)
    # uuids = [node['id'] for node in json_results['result']]
    # print(len(uuids))
    # for uuid in uuids:
    #     result=requests.delete(f'{base_url}nodes/{uuid}', auth=HTTPBasicAuth(user, password))
    #     print(result.status_code)
    
    # response = requests.get(f'{base_url}interfaces?gateway={gw_uuid}', auth=HTTPBasicAuth(user, password))
    # json_results = json.loads(response.text)
    # uuids = [interface['id'] for interface in json_results['result']]
    # print(len(uuids))
    # for uuid in uuids:
    #     result=requests.delete(f'{base_url}interfaces/{uuid}', auth=HTTPBasicAuth(user, password))
    #     print(result.status_code)
    

if __name__ == "__main__":
    main()
