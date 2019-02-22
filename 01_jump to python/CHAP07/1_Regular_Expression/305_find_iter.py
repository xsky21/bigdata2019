import re
original_text = "life is to short'"
p = re.compile("[a-z]+")
result =  p.finditer(original_text) #매칭 결과를 match object 리스트로 반환한다.

for r in result:
    print(r)
m = p.findall('life is to short') #검색 결과는 매칭된 문자열들을 리스트로 반환한다
print(m)
