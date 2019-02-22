import re
original_text = """"a1 asdkjjflewjrkjhwkejhqkjr
b3 asdlkfhwkejhrkjwehkjrhwjr
3k fqkwjehrkjwhrkjwqherkjwqhr
5j qkjwehrkjewqhrkjewqjherewkq
k4 qwjkerhkjwqehrjkewqhrkjqw
9p wqjerhkjweqherkjwehrjkewqh
u9 jhdjhrkjwherkjhwqekrehwjkr
"""

p = re.compile("[a-z][0-9]")
m = p.match(original_text) # 매칭이 된다. #대소문자 구분 중요ㅍ
print(m)
