#-*-coding: utf-8 -*-#
f = open("./sample.txt","r")
lines="".join(f)
f.close()

score = lines.split()
students=len(score)
total=0
for sco in range(0,students):
    total += int(score[sco])
average = total/students

f=open("./result.txt","w")
f.write(str(average))
f.close()
