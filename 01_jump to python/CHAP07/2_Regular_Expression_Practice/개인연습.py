import re
m = re.compile(r"a\bb")
p = m.search("a b")
print(p)