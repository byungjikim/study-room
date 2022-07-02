result = ''
for dan in range(2,21):
    result +="\n{}단!".format(dan)
    for i in range(1, 21,1):
        # print("{} * {} = {}".format(dan, i , dan*i))
        result += "{} * {} = {}".format(dan, i, dan*i)
print(result)


# print를 한 번에 출력하는 것이 효율적임
