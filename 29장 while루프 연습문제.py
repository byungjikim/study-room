'''
무한 에코 프로그램 작성하기
-> 일반적인 문자열을 입력하면 입력한 내용을 세 번씩 프린트함(공백을 붙여서)
 ex) Hello Hello Hello
-> help를 입력하면 "에코를 해주는 프로그램입니다."라는 문구가 떠야 함
-> quit을 누르면 "정말 종료하시겠습니까?(Y/N)"라는 문구가 떠야 함
-> Y를 누르면 종료 N을 누르면 계속 실행
'''
#for을 사용한다면 체험판임 몇 번 사용하면 끝이니까..
#정식 서비스는 While : 계속 써야

while(True):
    echo_program = input("메아리 쳐드립니다:")
    
    if echo_program == 'help':
        print("메아리 3번 쳐드려요")
        continue

    elif echo_program == 'quit':
        quit_pro = input("정말 종료하시겠습니까?(Y/N)")
        if quit_pro == 'Y':
            break
    
        elif quit_pro == 'N':
            continue
    
    else:
        print((echo_program+' ')* 3)
        break
