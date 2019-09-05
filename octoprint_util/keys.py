from time import sleep
import requests
import json

def probe(host):
    requests.packages.urllib3.disable_warnings()
    probe = requests.get(f'https://{host}/plugin/appkeys/probe', verify=False)

    if probe.status_code == 204:
        return True
    else:
        return False

def request(host, user=None):
    requests.packages.urllib3.disable_warnings()
    request = requests.post(f'https://{host}/plugin/appkeys/request', json={"app":"aquarium", "user":""}, verify=False)

    print(request.headers)

    return json.loads(request.text)

def check(host, key):
    status = False
    print(key)
    while not status:
        requests.packages.urllib3.disable_warnings()
        request = requests.get(f'https://{host}/plugin/appkeys/request/{key}', verify=False)
        print(request.status_code)
        if request.status_code == 200:
            return request.text
        elif request.status_code == 404:
            return 'Request timed out or access denied'
        elif request.status_code == 500:
            return "Server error"
        sleep(3)
