try:
    result = 4/2
    print(result)
    f=open("Na.txt","r")
    f.close()
except Exception as e:
    #모든 failure를 동일하게 처리하고 싶을 때 Exception의 유형을 정확히 모를 때 유용하다.(일반적인 상황에서 적용할 수 있는 tip)
    # 일반적인 상황에서 쓴다.

    print(e)

print("Program End")
