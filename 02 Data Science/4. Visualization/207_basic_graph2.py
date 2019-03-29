# 목적 : 하나의 차트에 다수의 그래프 기리기, 한글처리
import matplotlib.pyplot as plt

# plt.plot([1,2,3,4],[1,2,3,4]) # 직선으로 표현
plt.plot([1,2,3,4],[1,2,3,4],'ro') # 빨간 점으로 표현
# plt.plot([1,2,3,4],[1,2,3,4],'bo') # 파란 점으로 표현
# plt.plot([1,2,3,4],[1,2,3,4],'bx') # 파란 x로 표현
# plt.plot([1,2,3,4],[1,2,3,4],'bv') # 파란 세모로 표현
plt.xlabel('X-axis label') # X축 이름
plt.ylabel('Y-axis label') # Y축 이름
plt.show()