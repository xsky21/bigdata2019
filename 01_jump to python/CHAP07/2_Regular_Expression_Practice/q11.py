# 숫자 0 혹은  알파벳 b 여러 개가 알파벳 a 뒤에오는 문자열을 찾는 파이썬 프로그램을 만들어라
import re
def matching(answer):
    p = re.compile("[a-zA-Z]+[.,]*$") #괄호 안에" "이 들어갈수도 있고 메타문자가 들어갈 수도 있다
    m = p.search(answer)
    print(m)
matching("time is gold.")
matching("time")
matching("miss gold.")
matching("miss")
#여기선 b가 세 개일 때, b 세개를 출력해주지만. b2개를 출력시키고 싶다면 |를 써야된word
