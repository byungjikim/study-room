# 블로그 조회수 올리기 프로그램 for-loop-range example
import webbrowser
import time

list1 = ["https://maplestory.nexon.com/Promotion/event/2022/20220630/intro",
         "https://maplestory.nexon.com/Home/Main",
         "https://maplestory.nexon.com/News/Event"]
for i in list1:
    webbrowser.open(i) #사이트 열고 2초 쉬
    time.sleep(2)
