import re
p = re.compile('python') #findall의 결과와 동일 정규식에 최대한 많이 담는게 좋다
dest_str="""python one python
life is too short
python two
you need python
I will study python
"""

m = p.findall(dest_str)
print(m)