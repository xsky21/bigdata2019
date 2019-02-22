import re
m = re.compile(".*[@].*[.](com|net)")
p = m.search("park@naver.com")
q = m.search("lee@myhome.co.kr")
print(p)
print(q)