#1 집합 ABC

#A, B, C를 선언하라
a= set('aabbcahdhefgg')
b= set('ollkkmmhdhefi')
c= set('efggijjpnn')
#A와 B의 합집합

print('A와 B의 합집합:',a|b)

#A와 C의 차집합

print('A와 C의 차집합:',a-c)

#A와 B,C의 교집합
print('A와 B,C의 교집합:',a&b&c)

#2 과일 데이터
infruit = input("과일을 입력하세요:")
sfruit = infruit.split(' ')
print(set(sfruit))
