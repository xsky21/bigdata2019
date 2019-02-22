data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"): #사람별로 나누기 이때 생기는 empty string이 언제 사라지는지 잘 봐라
    word_result = []
    for word in line.split(" "): #이름과 주민번호를 나누기
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():#나눈 정보가 주민번호라면
            word = word[:6] + "-" + "*******" #주민번호 뒷자리를 별표 처리해라
        word_result.append(word) #다시 이름과 주민번호를 리스트에 넣어라
    result.append(" ".join(word_result)) #사람별로 정보를 합치고 다시 리스트에 넣는다.
print("\n".join(result)) #리스트에 넣은 사람별 정보를 줄넘김을 더해서 문자열로 뺀다. 이때 엠티 스트링이 사라진다.
