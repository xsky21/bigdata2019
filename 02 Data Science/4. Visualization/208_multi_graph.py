from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

# plt.plot([1,2,3,4],[1,2,3,4],'r-',[1,2,3,4],[3,4,5,6],'v-') -는 직선의 의미 기본색은 하늘색
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [3, 4, 5, 6])
plt.xlabel('X축 라벨')
plt.ylabel('Y축 라벨')
plt.show()