#f=open("새파일.txt","w") #현재 소스코드 파일이 있는 경로에 파일 생성. 유닉스 계열에서는 실행이 안될 수도 있다.
#f=open("d:\새파일.txt"."w") #절대경로에 파일 생성f=open("d:/새파일.txt"."w")
#f=open("d:\my_path\새파일.txt","w")
#f=open("d:/my_path/새파일.txt","w")
#f=open("d:\my_path\n새파일.txt","w") #이게 안되는 이유는 \n을 줄바꿈으로 인식한다.)
#f=open("d:\my_path\\new\새파일.txt","w") \\는\로 인식)
#f=open("d:\\my_path\\new\\새파일.txt","w") #실수를 줄이기위해서 모든\는 \\로 쓴다.
#f=open("d:/my_path/new/새파일.txt","w") #실수를 줄이기위해서 모든\는 \\로 쓴다.
#하위 버전과 연등이 되는지는 확인해야됨
f.close()
