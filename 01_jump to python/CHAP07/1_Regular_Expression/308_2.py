import re
original_text = """aslkdjfkljwlkejlkr
 asksjalkj"""
p = re.compile("[a-z]*\n [a-z]*", re.DOTALL)
m = p.match(original_text)
print(m)
