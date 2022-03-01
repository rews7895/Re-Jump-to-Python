"""
07-2. 정규 표현식 시작하기
  - 메타 문자: 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자.
  - . & $ * + ? { } [ ] \ ( ) 가 있다.
"""

"""
문자 클래스 []: [] 사이의 문자들과 매치
  - [abc]: 'a', 'b', 'c'중 한 개의 문자와 매치
  - a => Yes
  - before => Yes
  - dude => No

  - [a-c]: [abc] / [0-5]: [012345]
  - [a-zA-Z]: 알파벳 모두
  - [0-9]: 숫자

  - \d: 숫자와 매치, [0-9]와 동일한 표현식
  - \D: 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
  - \s: whitespace 문자(space나 tab처럼 공백을 표현하는 문자)와 매치, [\t\n\r\f\v]와 동일한 표현식이다.
        맨 앞의 빈칸은 공백 문자(space)를 의미
  - \S: whitespace 문자가 아닌 것과 매치, [^\t\n\r\f\v]와 동일한 표현식이다.
  - \w: 문자 + 숫자와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
  - \W: 문자 + 숫자가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

  #! 대문자로 사용된 것은 소문자의 반대임을 추츨할 수 있다.
"""

"""
Dot(.)
  - 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미
  - ex) a.b: a와 b 사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치
  - ex) a[.]b: a와 b사이에 Dot(.) 문자가 있으면 매치
"""

"""
반복(*)
  - * 바로 앞에 있는 문자가 0부터 무한대로 반복 될 수 있음
  - ca*t: * 문자 바로 앞에 있는 a가 0번 이상 반복되면 매치
  - ct => Yes
  - cat => Yes
  - caaat => Yes
"""

"""
반복(+)
  - +는 최소 1번 이상 반복될 때 사용.
  - ca+t: 문자 바로 앞에 있는 a가 1번 이상 반복되면 매치
  - ct => No
  - cat => Yes
  - caat => Yes
"""

"""
반복 {m, n}
  - {m}
    - ca{2}t: c + a(반드시 2번 반복) + t
    - cat: No
    - caat: Yes
  - {m, n}
    - m ~ n 반복되면 매치
    - cat: No
    - caat: Yes
    - caaaaat: Yes
  - ?
    - ab?c: b가 0 ~ 1번 사용되면 매치
    - abc: Yes
    - ac: Yes
"""

"""
정규 표현식을 지원하는 re 모듈
  - match(): 문자열의 처음부터 정규식과 매치되는지 조사한다.
  - search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
  - findall(): 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
  - finditer(): 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
"""
import re
# a = re.compile('ab*')

"""
match
  - 문자열의 처음부터 정규식과 매치되는지 조사한다.
  - 부합되면 객체를, 부합되지 않으면 None을 돌려준다.
  p = re.compile(정규 표현식)
  m = p.match('조사할 문자열')
  if m:
    print('Match found: ', m.group())
  else:
    print('No match')
"""
# b = re.compile('[a-z]+')

# m = b.match('python')
# print(m.group())
# m = b.match('3 python')
# print(m)

"""
search
  - 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
"""
# b = re.compile('[a-z]+')
# m = b.search('python')
# print(m)
# m = b.search('3 python')
# print(m)

"""
findall
  - 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
"""
# b = re.compile('[a-z]+')
# result = b.findall('life is too short')
# print(result)

"""
finditer
  - 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
"""
# b = re.compile('[a-z]+')
# result = b.finditer('life is too short')
# print(result)
# for r in result: 
#   print(r)

"""
match 객체의 메서드
  - group(): 매치된 문자열을 돌려준다.
  - start(): 매치된 문자열의 시작 위치를 돌려준다.
  - end(): 매치된 문자열의 끝 위치를 돌려준다.
  - span(): 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
"""
# b = re.compile('[a-z]+')
# m = b.match('python')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# m = b.search('3 python')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# m = re.match('[a-z]+', 'python')

"""
컴파일 옵션
  - DOTALL / S : dot 문자(.)가 줄바꿈 문자를 포함하여 모든 문자와 매치한다.
  - IGNORECASE / I : 대, 소문자에 관계없이 매치한다.
  - MULTILINE / M : 여러 줄과 매치한다. (^, $ 메타 문자의 사용과 관계가 있는 옵션이다.)
  - VERBOSE / X : verbose 모드를 사용한다. (정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수도 있다.)
"""
# # DOTALL
# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)

# p = re.compile('a.b', re.DOTALL)
# m = p.match('a\nb')
# print(m)

# # IGNORECASE
# p = re.compile('[a-z]', re.I)
# print(p.match('python'))
# print(p.match('Python'))
# print(p.match('PYTHON'))

# # MULTILINE
# # python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미이다.
# p = re.compile("^python\s\w+")

# data = """python one
# life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))

# p = re.compile("^python\s\w+", re.MULTILINE)

# data = """python on
# life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))

# VERBOSE, X
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# charref = re.compile(r"""
# &[#]        # Start of a numeric entity reference
# (
#   0[0-7]+         # Octal form
#   | [0-9]+        # Decimal form
#   | x[0-9a-fA-F]+ # Hexadecimal form
# )
# ;
# """, re.VERBOSE)

"""
백슬래시 문제
  - \문자가 문자열 자체임을 알려주기 위해 백슬래시 2개 (\\)를 사용하여 이스케이프 처리를 해야 한다.
"""
# p = re.compile('\\section')
# p = re.compile(r'\\section')