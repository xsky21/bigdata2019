import re
original_text = "life is to short'"
p = re.compile("[a-z]+")
m = p.search(original_text)
print(m)
m = p.findall('life is to short')
print(m)
