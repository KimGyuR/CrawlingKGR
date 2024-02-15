import requests
import urllib.request
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
from selenium import webdriver

# 시가 총액
html = requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html.text, 'html.parser')
driver = webdriver.Chrome()

# 크롤링 항목 7개
# 종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가

# 1 시가총액 메뉴에서 상위 10개 기업 정보 크롤링

# 2 각 회사별 URL 및 이름을 리스트에 저장, 코스피 상위 10개 기업의 URL 및 기업 이름을 리스트에 저장
# <a href=“/item/main.naver?code=005930”, class=“title”>삼성전자</a>
# <a href="/item/main.naver?code=000660" class="tltle">SK하이닉스</a>
# <a href="/item/main.naver?code=373220" class="tltle">LG에너지솔루션</a>
# <a href="/item/main.naver?code=207940" class="tltle">삼성바이오로직스</a>
# <a href="/item/main.naver?code=005380" class="tltle">현대차</a>
# <a href="/item/main.naver?code=005935" class="tltle">삼성전자우</a>
# <a href="/item/main.naver?code=000270" class="tltle">기아</a>
# <a href="/item/main.naver?code=068270" class="tltle">셀트리온</a>
# <a href="/item/main.naver?code=005490" class="tltle">POSCO홀딩스</a>
# <a href="/item/main.naver?code=035420" class="tltle">NAVER</a>


# 메뉴에서 선택한 기업의 세부 주식 정보를 화면에 출력
# 사용자가 -1을 입력할 때 까지 계속 반복함

print('-'*32)
print('[ 네이버 코스피 상위 10대 기업 목록 ]')
print('-'*32)

for i in range(10):
    print(f'{[i+1]} {}')

corp = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
if corp >= 1 and corp <=10:
    print(f'종목명: ')
    print(f'종목코드: ')
    print(f'현재가: ')
    print(f'전일가: ')
    print(f'시가: ')
    print(f'고가: ')
    print(f'저가: ')
elif corp == -1 :
    print('프로그램 종료')
else:
    print("다시 입력해 주세요")