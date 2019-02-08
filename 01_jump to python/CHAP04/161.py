f=open("./file3.txt","w", encoding='utf-8')#파이참에서 한글설정을 하려면 환경설정에서 file encoding을 euc-kr로 변경한다.
for i in range(1,11):
     data = "%d번째 줄입니다.\n"%i
     f.write(data)

f.close()