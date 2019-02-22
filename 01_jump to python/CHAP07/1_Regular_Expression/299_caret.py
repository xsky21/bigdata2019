import re
p = re.compile("[^0]")
m = p.match('1')
print(m)
p = re.compile("^") #그럼 이거 안나오는게 특수문자라서 그런게 아니네; 그냥 빈의미라서 매칭이 되는 거였네.
m = p.match('^')
print(m)
p = re.compile("[^a-zA-Z0-9]")
m = p.match('7')
print(m)

