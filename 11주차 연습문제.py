#1
list1= [1,2,3,'string']
list1 = list1 + ['a','b','c',1,2,3]
print('생선한 리스트에 원소 추가:',list1)
print(list1[1:4])
list1.index('string')
print('string의 위치:',list1.index('string'))
list1.count(1)

#2
char1 = "I love youm John!"
a= char1.split(" ")
a.index('John!') #!처리 어떻게함?=> 문제오류 but 자연어 처리시 조사 처리한댔는데.. 어케?
len(a)

