import re
# ^ .. $ 을 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')

print(tel_checker.match('02-123-4567'))
print(tel_checker.match('02-123-4567').group()) #전화번호만 나옴
print(tel_checker.match('053-321-32145'))
print(tel_checker.match('053950-4567'))

m = tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ', m.group())
print('group(0): ', m.group(0))
print('group(1): ', m.group(1))
print('group(2,3): ', m.group(2,3))
print('start(): ', m.start()) # 매칭된 문자열의 시작 인덱스
print('end(): ', m.end())     # 매칭된 문자열의 마지막 인덱스+1

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))

# 전방 긍정 탐색: (문자열이 won을 포함하고 있으면 won 앞의 문자열 리턴)
lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')
lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2)
# 전방 부정 탐색 (?!): 4자리 숫자 다음에 '-'를 포함하지 않으면 앞의 문자열 리턴
lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)

# 후방 긍정 탐색('am' 다음에 문자가 1개 이상 있으면, 해당 문자열 리턴)
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(lookbehind2)


# 후방 부정 탐색('\b': 공백)
# 공백 다음에 $기호가 없고 숫자가 1개 이상이고 공백이 있는 경우
lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind4)