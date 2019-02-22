# 숫자 0 혹은  알파벳 b 여러 개가 알파벳 a 뒤에오는 문자열을 찾는 파이썬 프로그램을 만들어라
import re
def matching(answer):
    p = re.compile("ab?")
    m = p.search(answer)
    print(m)

matching("abbbbbb")
matching("abbb")
matching("a")
matching("abb")
