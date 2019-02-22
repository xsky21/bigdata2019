import os

print(os.getcwd())
#print(os.system("dir"))
#os.system("notepad test.txt") 현재 경로에 test.txt가 없어서 해당 파일을 열 수 없고 새로 만들것인지를 물어본다.
os.chdir("d:/temp")
os.system("notepad test.txt")