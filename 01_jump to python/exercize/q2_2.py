#-*-coding: utf-8 -*-#
f = open("./sample.txt","r")
lines=f.readlines()
total = 0
#score = lines.split()
#students=len(score)
for line in lines :
    score = int(line)
    total += score

average = total/len(lines)

f=open("./result.txt","w")
f.write(str(average))
f.close()

print(lines)
