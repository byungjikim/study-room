'''
로봇 청소기의 행위를 if문으로 구현
x=0 우회전 출력
x= 1 점프 출력
x = -1 유턴 출력
난데모 나이 -> 전진 출력
'''
def robot_action(action):
    if action ==0:
        print("우회전")
    elif action == 1:
        print("JUMP")
    elif action == -1:
        print("U Turn")
    else:
        print("GOGO")
# action = int(input("action:"))
# if 반복은 자제하길 바람..
