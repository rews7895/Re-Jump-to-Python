"""
07-3. 강력한 정규 표현식의 세계로
"""
import re
"""
|
  - or과 동일한 의미로 사용된다
  - A|B라는 정규식이 있다면 A 또는 B라는 의미가 된다.
"""
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

"""
^
  - 문자열의 맨 처음과 일치함을 의미한다.
  - re.MULTILINE을 사용할 경우에는 여러 줄의 문자열일 때 각 줄의 처음과 일치하게 된다.
"""
# print(re.search('^Life', 'Life is too short'))
# print(re.search('^Life', 'My Life'))

"""
$
  - 문자열의 끝과 매치함을 의미
  - ^ 메타 문자와 반대의 경우.
"""
# print(re.search('short$', 'Life is too short'))
# print(re.search('short$', 'Life is too short, you need python'))

"""
\A
  - 문자열의 처음과 매치됨을 의미한다. 
"""

"""
\Z
  - 문자열의 끝과 매치됨을 의미한다.
"""

"""
\b
  - 단어 구분자이다. 보통 단어는 whitespace에 의해 구분된다.
"""
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

"""
\B
  - whitespace로 구분된 단어가 아닌 경우에만 매치된다.
  - \b 메타 문자와 반대의 경우이다. 
"""
# p = re.compile(r'\Bclass\B')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

"""
그루핑
  - 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하는 경우
  - 그룹을 만들어 주는 문자 ( ) 이다.
"""
# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# p = re.compile(r'(\w+)\s+((\d+)[-](\d+)[-](\d+))')
# m = p.search('park 010-1234-5678')
# print(m.group(5))

"""
그루핑된 문자열 재참조하기
  - 한 번 그루핑한 문자열을 재참조(Backreferences) 할 수 있다는 점.
  - \(num)은 참조하려는 그룹의 번호
"""
# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())

"""
그루핑된 문자열에 이름 붙이기
  - 그룹을 인덱스가 아닌 이름으로 참조
  - (?P<그룹 이름>...)
  - ex) (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
"""
# p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
# m = p.search('park 010-1234-5678')
# print(m.group('name'))

# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# print(p.search('Paris in the the spring').group())

"""
전방 탐색
  - 긍정형 전방 탐색 (?=...): ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
  - 부정형 전방 탐색 (?!...): ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
"""
# p = re.compile('.+:')
# m = p.search('http://google.com')
# print(m.group())

# p = re.compile('.+(?=:)')
# m = p.search('http://google.com')
# print(m.group())

"""
[^]: 문자클래스 안의 ^메타 문자는 반대를 의미함

  .*[.].*$ : 파일이름 + . + 확장자를 나타내는 정규식
  .*[.][^b].*$ : 확장자가 b라는 문자로 시작하면 안된다.
  .*[.]([^b]..|.[^a].|..[^t])$ : 첫 번째 문자가 b가 아니거나 두 번째 문자가 a가 아니거나 세 번째 문자가 t가 아닌 경우를 의미한다.
  .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$ : 확장자의 문자 개수가 2개여도 통과되는 정규식.
"""

"""
부정형 전방 탐색
  .*[.](?!bat$).*$
  .*[.](?!bat$|exe$).*$
"""

"""
문자열 바꾸기
  - sub 메서드는 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.
  - 딱 한번만 바꾸고 싶은 경우 count=1
  - subn: sub와 비슷하지만 반환 결과를 튜플로 돌려준다.(변경된 문자열, 바꾸기가 발생한 횟수)
"""
# p = re.compile('(blue|white|red)')
# print(p.sub('color', 'blue socks and red shoes'))
# print(p.sub('color', 'blue socks and red shoes', count=1))

# p = re.compile('(blue|white|red)')
# print(p.subn('color', 'blue socks and red shoes'))

"""
sub 메서드를 사용할 때 참조 구문 사용하기
"""
# p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
# print(p.sub('\g<phone> \g<name>', 'park 010-1234-5678'))
# print(p.sub('\g<2> \g<1>', 'park 010-1234-5678'))

"""
sub 메서드의 매개변수로 함수 넣기
"""
# def hexrepl(match):
#   value = int(match.group())
#   return hex(value)

# p = re.compile(r'\d+')
# print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))

"""
Greedy vs Non-Greedy
"""
# s = '<html><head><title>Title</title>'
# print(len(s))
# print(re.match('<.*>', s).span())
# print(re.match('<.*>', s).group())

# print(re.match('<.*?>', s).group())