#-*-coding: utf-8 -*-#
f=open("./방명록.txt","r")
namelst = "".join(f)
namelist = namelst.split()
f.close()

name=input("이름을 입력하세요: ")

def search_visitor(name):
    if name in namelist:
        print(name+"님 다시 방문해주셔서 감사합니다. 즐거운 시간 되세요")
        return name
    elif name not in namelist:
        birth = input("생년원일을 입력하세요 (예:801212) : ")
        f=open("./방명록.txt","a")
        f.write("\n"+name+" "+birth)
        f.close()

        print(name+"님 환영합니다. 아래 내용을 입력했습니다.")
        print(name+" "+birth)
        return ""
search_visitor(name)

