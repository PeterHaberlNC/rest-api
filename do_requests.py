import requests
import socket
import datetime
import argparse

# Erstelle einen Argumentparser
parser = argparse.ArgumentParser(description='Anzahl messages und URL')
parser.add_argument('number', type=int, help='Iterations')
parser.add_argument('text', type=str, help='Payload')

# Lese die Argumente von der Kommandozeile
args = parser.parse_args()
url = args.text

#http://182.92.141.163:8000//api/analytics
#url = "https://flow-poc.apps.ocp420241004074046.openshiftlabs.online/api/analytics"
#url = "http://182.92.141.163:8000/api/analytics"

timestamp = datetime.datetime.now().isoformat()
local_ip = socket.gethostbyname(socket.gethostname())
data = {
    "timestamp": timestamp,
    "local IP": local_ip
}

for i in range(args.number):
    response = requests.post(url, json=data, verify=False)
    # Print the response
    print(response.json())
