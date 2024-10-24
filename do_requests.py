import requests
import socket
import datetime

#http://182.92.141.163:8000//api/analytics
#url = "https://flow-poc.apps.ocp420241004074046.openshiftlabs.online/api/analytics"
url = "http://182.92.141.163:8000//api/analytics"

timestamp = datetime.datetime.now().isoformat()
local_ip = socket.gethostbyname(socket.gethostname())
data = {
    "timestamp": timestamp,
    "local IP": local_ip
}

for i in range(10):
    response = requests.post(url, json=data, verify=False)
    # Print the response
    print(response.json())
