# urllib.request.urlopen(url): 해당 url에서 html파일이나
#                              이미지 파일, 기타 파일을 가져오는 함수
# HTTPResponse.read(): HTML 콘텐츠를 읽음
from urllib.request import urlopen

html = urlopen('http://www.daangn.com/hot_articles')
print(type(html))
print(html.read())