import re
p = re.compile("[a-z]+")
m = p.search('3 python')
print(m)
if m:
    print('Match founded: ', m.group()) #여기서 콤마의 의미 주목할 것
else:
    print("No result")