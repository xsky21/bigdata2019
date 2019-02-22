import re
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+') #반드시 r을 사용해야하는 것은 아니다. 사용하지 않는 게 더 좋음
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
