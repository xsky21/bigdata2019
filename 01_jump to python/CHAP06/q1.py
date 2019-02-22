data = (input("알파벳을 넣으시오 : "))
times=1
for n in range(0,len(data)):
    if n == 0:pass
    elif n == len(data)-1:
        if data[n] != data[n-1]:
            print(data[n-1]+str(times),end="")
            print(data[n]+"1")
        else:
            times+=1
            print(data[n]+str(times))
    elif data[n] == data[n-1]:
        times+=1
    elif data[n] != data[n-1]:
        print(data[n-1]+str(times),end="")
        times =1
