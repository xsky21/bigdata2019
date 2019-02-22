#어떤 문자열을 입력했을 때, 특정한 문자열 매치시키는 파이썬 프로그램을 짜라
import re
def marking(answer):
    p = re.compile("\w*")
    m = p.match(answer)
    print(m)

marking("mkwerwern")
