'''
구글 입사 문제
1부터 10,000까지 8이라는 숫자가 총 몇 번 나오는가?
8이 포함되어 있는 숫자의 개수를 카운팅 x 8이라는 숫자를 모두 카운팅
예를들어 8808= 3 8888=4
'''
#1부터 1만까지 1간격으로 range 하고
#각 숫자를 str으로 받아서 list 넣고
#8 개수 조회
#내 답
a=0
for i in range(1, 10001):
    i_list = list(str(i))
    eight_i = i_list.count('8')
    a += eight_i

print(a)


'''
list에 굳이 넣어서 카운트 안해도
for문에서 string 넣으면 하나씩 쪼개서 실행하므로
그 쪼개는 것에서 조건문 주면 해결 가능한 것임.
'''

#선생님 답
count = 0
for i in range(1,10000):
    for j in str(i):
        if j == '8':
            count += 1
print(count)

'''구글의 의도한 답
8XXX
X8XX
XX8X
XXX8

각 000~999 => 1000가지의 경우의 수'''
