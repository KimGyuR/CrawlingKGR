import re

# compile() 사용 안함
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))

# compile() 사용
p = re.compile('[a-z]+') # 알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

m = re.match('[a-z]+', 'pythoN') # 소문자가 1개 이상
print(m)

m = re.match('[a-z]+', 'PYthon') # 소문자가 1개 이상
print(m)

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython')) # 문자열 처음에 공백 포함

print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN')) # $: 문자열의 마지막 부분 검사

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))

p = re.compile('[a-z]+') # 알파벳 소문자

print(p.findall('life is too short! Regular expression test'))

result = p.search('I like apple 123')
print(result)
print(result.group()) # group(): 일치하는 전체 문자열 리턴

result = p.findall('I like apple 123')
print(result)

