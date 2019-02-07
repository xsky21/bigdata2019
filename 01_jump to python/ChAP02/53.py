# coding: cp949
input_data="201901300915-0175440.002"
year="올해는 " + input_data[0:3] + "년입니다."
month="이번 달은 " + input_data[4:5] + "월입니다."
day="오늘은 " + input_data[6:7] + "일입니다."
time="지금 시각은 " + input_data[8:9]+"시 "+input_data[10:11]+"분입니다"
temp=input_data[12:13]
print(year)
print(month)



