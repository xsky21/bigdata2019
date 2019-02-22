import re
p = re.compile("[\d]") # [0-9]
m = p.match('1')
print(m)
p = re.compile("[한]긁") # [0-9]
m = p.match('한글')
print(m)
p = re.compile("[ ]") # = [\s] = ' '
m = p.match(' 한')
print(m)
p = re.compile("[ ]") # = [\s] = ' '
m = p.match(' 한')
print(m)

