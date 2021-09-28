import requests

URL = 'http://straw.sandbox.kakaoi.io/boxes/daejung-high-school/notice_v01' 
response = requests.get(URL) 

print('code:', response.status_code) 
print('text:', response.text)
