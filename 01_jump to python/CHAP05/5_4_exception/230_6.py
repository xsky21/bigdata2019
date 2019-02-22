input_denominator = int(input("분모를 입력하세요: "))
try:
    result = 4/input_denominator
    print(result)
    f=open("Na.txt","r")
    f.close()
except ZeroDivisionError as e:
    #모든 failure를 동일하게 처리하고 싶을 때 Exception의 유형을 정확히 모를 때 유용하다.(일반적인 상황에서 적용할 수 있는 tip)
    print(e)
    print("분\모가 0이 되어서 안됩니다. 다시 입력하세요.")
except FileNotFoundError as e:
    print(e)
    print("해당 파일이 존재하지 않습니다. 230_6.py가 있는 경로에 NA.TXT파일이 있는지 확인하세요")



print("program end")
