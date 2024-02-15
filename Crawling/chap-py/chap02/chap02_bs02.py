html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examlpes!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
# 태그를 사용하여 요소에 직접 접근하기
# <title> 태그에 접근(soup.태그명)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.string) # <title> 태그의 텍스트만 리턴
print(soup.title.get_text()) # .string, .text(예전 버전)와 동일한 기능

# 태그명.parent: 해당 태그를 포함하고 있는 부모
print(soup.title.parent)

# <body>태그에 접근
print(soup.body)

# <h1>태그 접근: 동일한 태그가 여러개일 경우, 첫번째 요소 추출
print(soup.h1)
print(soup.h1.string)

# <a>태그 접근
print(soup.a)
print(soup.a.string)        # <a> 태그 내부의 텍스트 추출 (google)
print(soup.a['href'])       # <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href'))   # a['href']와 동일 기능

# find()함수: 해당 조건에 맞는 맨 처음 검색 결과를 추출
print(soup.find('div'))

# 여러 <div> 태그 중 특정 속성을 가지는 항목 추출
print(soup.find('div', {'id':'text_id2'}))

# 추출된 요소에서 텍스트만 가져옴
div_text = soup.find('div', {'id':'text_id2'})
print(div_text.text)

# <a> 태그 및 <a> 태그의 href 속성 추출
href_link = soup.find('a', {'class': 'internal_link'}) # 딕셔너리 형태
href_link = soup.find('a', class_='internal_link') # class_사용: class는 파이썬 예약어

print(href_link)
print(href_link['href']) # <a>태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href')) # ['href']와 동일 기능
print(href_link.text) # <a> Page1 </a> 태그 내부의 텍스트(Page1) 추출

# attrs: <a>태그 내부의 모든 속성 가져오기
print('href_link.attrs: ', href_link.attrs) # <a>태그 내부의 모든 속성 출력
print('class 속성값: ', href_link['class'])  # class 속성의 value 출력

print('values(): ', href_link.attrs.values()) # 모든 속성들의 값 출력

values = list(href_link.attrs.values()) # dictionary 값들을 리스트로 변경
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))


href_value = soup.find(attrs={'href': 'www.google.com'})
href_value = soup.find('a', attrs={'href': 'www.google.com'})

print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)


span_tag = soup.find('span')

print('span tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.string)

print('class 속성값: ', href_link['class'])