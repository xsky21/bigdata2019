import re
original_text = """1a asdkjjflewjrkjhwkejhqkjr
b3 asdlkfhwkejhrkjwehkjrhwjr
3k fqkwjehrkjwhrkjwqherkjwqhr
5j qkjwehrkjewqhrkjewqjherewkq
k4 qwjkerhkjwqehrjkewqhrkjqw
9p wqjerhkjweqherkjwehrjkewqh
u9 jhdjhrkjwherkjhwqekrehwjkr
"""

p = re.compile("1a [a-z]+\Sb3", re.DOTALL)
m = p.match(original_text)
print(m)
