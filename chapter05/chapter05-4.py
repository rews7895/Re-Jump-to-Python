"""
05-4. 예외 처리
  - try, except를 사용
  - try 블록 수행 중 오류가 발생하면 except 블록이 수행
  -
    try:
      ...
    except 발생오류 as 오류 메세지 변수:
    # try문을 수행한 후 예외 발생 여부와 상관없이 finally절을 거침
    finally:
"""
# f = open('나없는파일', 'r')

# try:
#   4 / 0
# except ZeroDivisionError as e:
#   print(e)

# 여러개의 오류 처리
# try:
#   a = [1, 2]
#   print(a[3])
#   4/0
# except ZeroDivisionError as e:
#   # print('0으로 나눌 수 없습니다.')
#   print(e)
# except IndexError as e:
#   # print('인덱싱할 수 없습니다.')
#   print(e)

# 2개 이상의 오류를 동시에 처리하기 위해서는 괄호를 이용해 함께 묶어 처리한다.
# try:
#   a = [1, 2]
#   print(a[3])
#   4 / 0
# except (ZeroDivisionError, IndexError) as e:
#   print(e)

# 오류 회피
# try:
#   f = open('없는파일', 'r')
# except FileNotFoundError:
#   pass

# 오류 일부러 발생시키기
# class Bird:
#   def fly(self):
#     raise NotImplementedError

# class Eagle(Bird):
#   def fly(self):
#     print('very fast')

# eagle = Eagle()
# eagle.fly()

# 예외 만들기
# class MyError(Exception):
#   def __str__(self):
#     return '허용되지 않는 별명입니다.'

# def sayNick(nick):
#   if nick == '바보':
#     raise MyError()
#   print(nick)

# try:
#   sayNick('천사')
#   sayNick('바보')
# except MyError as e:
#   print('허용되지 않는 별명입니다.')
#   print(e)