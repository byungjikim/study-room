f= open('파일명.txt.','w') #새로 열어서 덮어 씀
f.write('Welcome guys.\n')
f.close()

f= open('파일명.txt.','a') #파일 추가
f.write('두번 째 줄입니다.\n')
f.close()

f= open('파일명.txt.','r')
data_read = f.read()
f.close()
