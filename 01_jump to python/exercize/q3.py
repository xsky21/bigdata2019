#-*-coding: utf-8 -*-#
f=open("./연습생.txt","r")
candi = "".join(f)
candilist = candi.split()
f.close()

def show_candidated(candidate_list):
    print(candilist)
def make_idol(candidate_list):
    for a in candilist:
        print("아이돌 "+a+" 인기 급상승")
def make_world_star(candidate_list):
    for b in candilist:
        print("아이돌 "+b+" 월드스타 등극")

show_candidated(candilist)
make_idol(candilist)
make_world_star(candilist)


