"""
05-5. 내장 함수
"""

"""
abs: 숫자를 입력받고, 그 숫자의 절댓값을 리턴
"""
# print(abs(-3))

"""
all: 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
"""
# print(all([1, 2, 3]))
# print(all('123'))
# print(all(1))

"""
any: any(x)는 x중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때만 False를 돌려준다
"""
# print(any([1, 2, 3, 0]))
# print(any['', 0])

"""
chr: 아스키(ASCII)코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
"""
# print(chr(97))
# print(chr(48))

"""
dir: 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
"""
# print(dir([1, 2, 3]))
# print(dir({'1': 'a'}))

"""
divmod(a, b): 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
"""
# print(divmod(7, 3))

"""
enumerate: 함수는 수서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate객체를 돌려준다.
  - foreach($items as $key => $item)와 같이 쓸 수 있을 듯?
"""
# for i, name in enumerate(['body', 'foo', 'bar']):
#   print(i, name)

"""
eval(expression): 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수
"""
# print(eval('1+2'))
# print(eval("'hi' + 'a'"))
# print(eval('divmod(4, 3)'))

"""
filter: 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
"""
# def positive(x):
#   return x > 0

# print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

"""
hex: 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수
"""
# print(hex(234))
# print(hex(3))

"""
id: 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수
"""
# a = 3
# print(id(a))
# print(id(3))
# b = a
# print(id(b))

"""
input: 사용자의 입력을 받는 함수
"""
# a = input('Enter: ')

"""
int: 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
  - int(x, radix)는 radix진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
"""
# print(int('3'))
# print(int(3.4))
# print(int('11', 2))
# print(int('1A', 16))

"""
isinstance(object, class): 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 
  - 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
"""
# class Person: pass

# a = Person()

# print(isinstance(a, Person))

"""
len: 입력값 s의 길이를 돌려주는 함수
"""
# print(len('python'))
# print(len([1, 2, 3]))
# print(len(1, 'a'))

"""
list: 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
"""
# print(list('python'))
# print(list((1, 2, 3)))
# a = [1, 2, 3]
# b = list(a)
# print(b)
# print(id(a))
# print(id(b))

"""
map(f, iterable): 함수와 반복 가능한 자료형을 입력 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
"""
# def twoTimes(x): return x * 2

# print(list(map(twoTimes, [1, 2, 3, 4])))

# 람다 식으로 변환
# print(list(map(lambda a: a * 2, [1, 2, 3, 4])))

"""
max: 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
"""
# print(max([1, 2, 3]))
# print(max('python'))

"""
min: 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
"""
# print(min([1, 2, 3]))
# print(min('python'))

"""
oct: 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
"""
# print(oct(34))
# print(oct(12345))

"""
open: 파일이름과 읽기방법을 입력 받아 파일 객체를 돌려주는 함수
  - w: 쓰기 모드 / r: 읽기 모드 / a: 추가 모드 / b: 바이너리 모드
"""
# f = open('binary_file.txt', 'rb')
# fread = open('read_mode.txt', 'r')
# fread2 = open('read_mode.txt')
# fappend = open('append_mode.txt', 'a')

"""
ord: 문자의 아스키 코드 값을 돌려주는 함수
"""
# print(ord('a'))
# print(ord('0'))

"""
pow(x, y): x의 y제곱한 값을 돌려주는 함수
"""
# print(pow(2, 4))
# print(pow(3, 3))

"""
range
  - 인수가 하나: 0 ~ n
  - 인수가 둘: start ~ end
  - 인수가 셋: 둘일 때, 숫자 사이의 거리
"""
# print(list(range(5)))
# print(list(range(5, 10)))
# print(list(range(1, 10, 2)))

"""
round: 숫자를 입력받아 반올림해 주는 함수
"""
# print(round(4.6))
# print(round(4.2))
# print(round(5.678, 2))

"""
sorted: 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수
  - 리스트 자료형의 sort함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.
"""
# print(sorted([3, 1, 2]))
# print(sorted(['a', 'b', 'c']))
# print(sorted('zero'))
# print(sorted((3, 2, 1)))

"""
str: 문자열 형태로 객체를 변환하여 돌려주는 함수
"""
# print(str(3))
# print(str('hi'))
# print(str('hi'.upper()))

"""
sum: 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
"""
# print(sum([1, 2, 3]))
# print(sum((4, 5, 6)))

"""
tuple: 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
"""
# print(tuple('abc'))
# print(tuple([1, 2, 3]))
# print(tuple((1, 2, 3)))