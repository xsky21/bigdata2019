import re
p = re.compile('.*python$',re.MULTILINE)
dest_str="""python one
life is too short
python two
you need python
I will study python
"""

m = p.findall(dest_str)
print(m)