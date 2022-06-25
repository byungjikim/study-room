numbers = input("숫자를 4개를 공백으로 구분해서 넣어주세요:")
a,b,c,d = numbers.split(" ")
e= int(a)+int(b)+int(c)+int(d)
print("{}, {}, {}, {}의 합은 {}이다.".format(a,b,c,d,e))
