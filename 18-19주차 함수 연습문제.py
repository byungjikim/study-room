import requests
import json

def add_num2():
    a=input('띄워쓰기로 나눠서 숫자를 4개 입력하시오:')
    nums = a.split(' ')
    return print(int(nums[0])+int(nums[1])+int(nums[2])+int(nums[3]))
    
'''
선생님풀이
def add_num2():
    list1 = input("띄워쓰기로 나눠서 숫자를 4개 입력하시오:")
    a,b,c,d = list1.split()
    a,b,c,d = int(a),int(b),int(c),int(d)
    return a+b+c+d
'''


def getLocation():
    domain_name = input('domain name을 입력하세요:')
    url = 'http://ip-api.com/json/'+domain_name
    response = requests.get(url)
    dict1 = json.loads(response.text)
    print('실제 위치:',dict1['country'],dict1['regionName'],dict1['city'])

add_num2()
getLocation()

'''
선생님풀이
def getLocation(ip):
    url = 'http://ip-api.com/json/'+ip
    response = request.get(url)
    return respnse.json()
'''
