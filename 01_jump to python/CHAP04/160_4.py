f=open("./file3.txt","w")
f.write("Hello World!!!!!!!!!!!!") #2번 라인 수정 후 주석처리하고 재실행시 메시지는 overwrite 된다.
for i in range(1,11):
     data = "%d번째 줄입니다.\n"%i
     f.write(data)

f.close()