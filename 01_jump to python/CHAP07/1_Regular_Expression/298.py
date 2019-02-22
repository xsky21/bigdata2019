import re
#p = re.compile("[abc]")
#m = p.match("a")
#print(m) # 매칭이 된다.
#p = re.compile("[abc]")
#m = p.match("k")
#print(m) # 매칭이 안된다.
#p = re.compile("[abc]")
#m = p.match("before") #첫글짜에 b가 있어서 매칭
#print(m)
#p = re.compile("[abc]") #첫글짜에 abc가 없어서
#m = p.match("dude")
#print(m)
#p = re.compile("[abc]")
#m = p.match("a")
#print(m) # 매칭이 된다.
#p = re.compile("[abc]")
#m = p.match("dad") # 매칭이 안된다.
#print(m) # 매칭이 된다.
#p = re.compile("[def]")
#m = p.match("dad")# 된다.
#print(m)
p = re.compile("d[def]") #조건 : 두글자 이상이고 첫번째는 d, 두번째는 def 셋중 하나다.
m = p.match("dad") #이건 왜 매칭이 안되지?
print(m)
p = re.compile("d[abc]") #조건 : 두글자 이상이고 첫번째는 d, 두번째는 abc 셋중 하나다.
m = p.match("dad")
print(m)
p = re.compile("d[abc]a") #세글자 이상이고 처음은 d 중간은 abc 둘중 하나 마지막은 a인 문자열
m = p.match("dad") #이건 왜 매칭이 안되지?
print(m)
p = re.compile("[abc]d")
m = p.match("dad")
print(m)
p = re.compile("[\D][\D][\D]")
m = p.match("dad")
print(m)
p = re.compile("[\s][a-z]")
m = p.match(" a")
print(m)
p = re.compile("[cd][ab]")
m = p.match("da")
print(m)
p = re.compile("[][ad]")
m = p.match(" d")
print(m)

