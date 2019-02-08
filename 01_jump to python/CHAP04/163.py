f=open("./file3.txt","r" ,encoding='utf-8')
line=" "
while line:
    line = f.readline()
    print(line,end=" ")
f.close()