"""
04-1. 함수
"""

# def add(a, b):
#   return a + b

# a = 3
# b = 4
# c = add(a, b)
# print(c)

# def say():
#   return 'Hi'

# print(say())

# a = 3
# b = 4
# def add(a, b):
#   print(f'{a} + {b}의 합은 {a + b}입니다.')
# add(a, b)

# 리턴 값이 없음.
# result = add(a = 3, b = 7)
# print(result) 

# 여러개의 값을 받는 함수
# def addMany(*args):
#   result = 0
#   for i in args:
#     result = result + i
#   return result

# result = addMany(1, 2, 3, 4, 5)
# print(result)
# result = addMany(1, 2, 3)
# print(result)

# def addMul(choice, *args):
#   if choice == 'add':
#     result = 0
#     for i in args:
#       result = result + i
#   elif choice == 'mul':
#     result = 1
#     for i in args:
#       result = result * i
#   return result

# result = addMul('add', 1, 2, 3, 4, 5)
# print(result)

# result = addMul('mul', 1, 2, 3, 4, 5)
# print(result)

# 키워드 파라미터
# def printKwargs(**kwargs):
#   print(kwargs)

# printKwargs(a = 1)
# printKwargs(name = 'foo', age = 3)

# 함수의 결괏값은 언제나 하나이다. -> 두 가지면 튜플로 리틴받거나 리턴 받는 변수를 개수맞춰서 선언.
# def addAndMul(a, b):
#   return a + b, a * b

# result = addAndMul(3, 4)
# print(result)
# result1, result2 = addAndMul(3, 4)
# print(result1)
# print(result2)

# def sayNick(nick):
#   if nick == '바보':
#     return
#   print(f'나의 별명은 {nick}입니다.')

# sayNick('콥')
# sayNick('바보')

# 매개변수에 초깃값 미리 설정하기
# def sayMyself(name, old, man = True):
#   print(f'나의 이름은 {name}입니다.')
#   print(f'나이는 {old}살 입니다.')
#   if man:
#     print('남자입니다.')
#   else:
#     print('여자입니다.')

# sayMyself('박귀도', 27)
# sayMyself('이로섬', 28, False)

# 함수의 범위
# a = 1
# def vartest(a):
#   a = a + 1

# vartest(a)
# print(a)

# a = 1
# def vartest(a):
#   a = a + 1
#   return a

# a = vartest(a)
# print(a)

# 글로벌 명령어 사용하기
# a = 1
# def vartest():
#   global a
#   a = a + 1

# vartest()
# print(a)

# lambda: 함수를 한줄로 간결하게 만들 때 사용한다.
# add = lambda a, b: a + b
# result = add(3, 4)
# print(result)