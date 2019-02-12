def sum2(a,b):
    return a+b

def safe_sum2(a,b):
    if type(a) != type(b):
        print("두 인자의 형이 다릅니다.")
        return
    else:
        result = sum2(a,b)
    return result

if __name__=="__main__": #테스트용 명령임을 나타내는 것
# 같은 파일 안에선 __name__은 __main__으로 세팅된다. 이 뜻은 다른 파일에선 안된다는 것.
    print(sum2(1,2))
    print(safe_sum2(1,2))
    print(safe_sum2(1,"2"))