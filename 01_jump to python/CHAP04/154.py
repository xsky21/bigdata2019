a=1 #전역변수
#전역변수는 힙이라는 저장공간에 들어가며, 끝날 때까지 유효하다.
def vartest(a): #b는 지역변수
    a=a+1
    return a
print(vartest(a))