import requests
import json


domain_name = input('domain name:')
url = 'http://ip-api.com/json/'+domain_name

response = requests.get(url)
dict1 = json.loads(response.text)
for i in dict1.keys():
    print(i,':',dict1[i])
#dictionary로 만들었다!! 원래 str이었는데
