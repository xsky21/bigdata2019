# 숫자 0 혹은  알파벳 b 여러 개가 알파벳 a 뒤에오는 문자열을 찾는 파이썬 프로그램을 만들어라
import re
p = re.compile('(?=[.])0+')
m = p.search("123.08.004.69")
#m = p.sub("", "123.08.004.69")
print(m)