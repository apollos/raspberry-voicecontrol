import requests
import json

url = "https://www.google.com/speech-api/v2/recognize"
payload = {'output':'json', 'lang':'zh-cn', 'key':'AIzaSyDUyyWa9Nj1aPnS_9DJsjqrrgQ6OEUHMaU'}
headers = {'Content-Type':'audio/x-flac; rate=16000;'}
audioFiles = {'file':open('standup.flac', 'rb')}
r = requests.post(url, headers=headers, params=payload, files=audioFiles)
print(r.text)
r.json()
