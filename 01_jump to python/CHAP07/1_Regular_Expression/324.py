import re
p = re.compile('(blue|white|red)')
print(p.subn('colour','blue socks and red shoes'))
