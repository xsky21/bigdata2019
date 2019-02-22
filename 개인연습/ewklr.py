import re
p = re.compile("^[a-z]+")
m = p.search("33 python")
print(m)