import re
p = re.compile("[\w]")
m = p.match('1')
print(m)
p = re.compile("..") # [] 문자열 클래스가 아닌 일반 문법으로 사용했을 경우, '.'는 모든 문자를 의미한다.
m = p.match('dad')
print(m)
# 정규표현식은 깔때기라고 생각하자.
p = re.compile(".")
m = p.match('da')
print(m)
p = re.compile(".")
m = p.match('pen.')
print(m)
p = re.compile("...[.]")
m = p.match('peni')
print(m)
p = re.compile("...[.]") #'.'를 메타 문자가 아닌 고유의 문자의미로 정규식을 사용하고 싶다면 .를 문자열 클래스[]안에서 사용해야 한다.
m = p.match('peni')
print(m)
p = re.compile("a[b]c")
m = p.match('abc')
print(m)

