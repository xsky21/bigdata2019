#pip install bs4      cmd 에서 bs4를 설치하는 것
#웹크롤링은 html구조를 바로 분석하는 것
from bs4 import BeautifulSoup

html='''
<html>
Naver 실시간 영화 순위
<td class="title">
<div class="tit3">
<a title="1위 영화">
</a>
</div>
</td>
</html>
''' #따옴표 세개 붙이는 이유는 줄을 바꾸었기 때문

soup = BeautifulSoup(html, 'html.parser')
print(soup)
tag=soup.td #수프 밑에 있는 td 태그를 읽는건가?
print("\nsoup.td")
print(tag)

tag = soup.div
print("\nsoup.div")
print(tag)

tag = soup.a
print("\nsoup.a")
print(tag)

print("\ntag.name")
print(tag.name)

print("\ntag.attrs")
print(tag.attrs) #딕셔너리 형태로 속성 값을 출력한다)

print("\ntag.text")
print(tag.text) #태그의 텍스트를 출력한다

print("\ntag.string")
print(tag.string) #태그의 텍스트를 출력한다 시스템의 오류로 여기도 통하는 것.
pass

