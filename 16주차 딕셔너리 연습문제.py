'''
dict b에서 name 데이터를 찾으라1
dict b에서 birth 데이터를 101010으로 바꿔라2
dict b에서 key가 city이고 value가 Seoul인 데이터를 추가하라3
'''

#1
dict_b = {'name':'John',
          'phone':'01012345432',
          'email':'test@test.com',
          'birth':111111}
print(dict_b)
print('name:',dict_b['name'])

#2
dict_b['birth']=101010
print('revised birth:',dict_b['birth'])

#3
dict_b['city']='Seoul'
print('complemetary information of city:',dict_b['city'])

#4 추가문제 지우는 것 del
del dict_b['email']
print(dict_b)
