def add(number_list):
    sum = 0
    for a in number_list:
        sum = sum+a
    return sum

a = [1,4,6,2,1]
b = [1,5,4,5,2]

print(sum(a))
print(sum(b))

#navi = cat()
#이 것을 읽는 방법은 두가지
#"navi는 객체", "navi는 cat의 인스턴스 = navi는 클래스 cat을 이용하는 변수다",
# 클래스 내 함수의 첫번째 인수는 무조건 self