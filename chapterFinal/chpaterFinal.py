"""
Q1. 문자열 바꾸기
  a:b:c:d
  문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오
  a#b#c#d
"""
# txt = 'a:b:c:d'
# print('#'.join(txt.split(':')))

"""
Q2. 딕셔너리 값 추출하기
  다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
  a = {'A': 90, 'B': 80}
  a['C']
  a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다. 'C'에 해당하는 key 값이 없을 경우 
  오류 대신 70을 얻을 수 있도록 수정하시오.
"""
a = {'A': 90, 'B': 80}

# try:
#   print(a['C'])
# except KeyError as e:
#   a['C'] = 70
#   print(a['C'])

# ======================
# print(a.get('c', 70))


""" *
Q3. 리스트의 더하기 extend 함수
  다음과 같은 리스트 a가 있다.
  a = [1, 2, 3]
  리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.

  a = [1, 2, 3]
  a = a + [4, 5]
  print(a)
  >>>>> [1, 2, 3, 4, 5]

  a = [1, 2, 3]
  a.extend([4, 5])
  print(a)
  >>>>> [1, 2, 3, 4, 5]
  + 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을끼? 있다면 그 차이점을 설명하시오.


  - extend를 사용하면 주소 값이 변하지 않고, +는 주소 값이 변한다.
"""


"""
Q4. 리스트 총합 구하기
  다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오
  A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
"""
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# print(sum(filter(lambda num: num >= 50, A)))

"""
Q5. 피보나치 함수
  첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
  0, 1, 1, 2, 3, 4, 8, 13...
  입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 출력하는 함수를 작성해보자.
"""
# n = 143
# li = [0, 1]
# while li[len(li) - 1] + li[len(li) - 2] <= n:
#   li.append(li[len(li) - 1] + li[len(li) - 2])

# print(sum(li))

"""
Q6. 숫자의 총합 구하기
  사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오.(단 숫자는 콤마로 구분하여 입력한다.)
  65,45,2,3,45,8
"""
# a = '65,45,2,3,45,8'
# li = a.split(',')
# li = list(map(int, li))
# print(sum(li))

"""
Q7. 한 줄 구구단
  사용자로부터 2 ~ 9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오
  실행 예)
    구구단을 출력할 숫자를 입력하세요(2 ~ 9): 
    2 4 6 8 ... 16 18
"""
# i = int(input('구구단을 출력할 숫자를 입력하세요(2 ~ 9): '))
# if i > 0 and i <= 9:
#   for j in range(1, 10):
#     print(i * j)
# else:
#   print('2 ~ 9까지의 숫자를 입력해주세요.')

"""
Q8. 역순 저장
  다음과 같은 내용의 파일 abc.txt가 있다.
  AAA
  BBB
  CCC
  DDD
  EEE

  이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오
  EEE
  DDD
  CCC
  BBB
  AAA
"""
# f = open('chapterFinal/abc.txt', 'r')
# data = f.read()
# f.close()

# li = data.split('\n')
# li.reverse()

# f = open('chapterFinal/abc.txt', 'w')
# for line in li:
#   f.write(line)
#   f.write('\n')
# f.close()


"""
Q9. 평균값 구하기
  오른쪽과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 
  평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오
  70
  60
  55
  75
  95
  90
  80
  80
  85
  100
"""
# import statistics

# f = open('chapterFinal/sample.txt', 'r')
# data = f.read()
# f.close()
# li = data.split('\n')
# li = list(map(int, li))

# print(statistics.mean(li))

"""
Q10. 사칙연산 계산기
  다음과 같이 동작하는 클래스 Calculator를 작성하시오.
  cal1 = Calculator([1, 2, 3, 4, 5])
  cal1.sum()
  >>> 15
  cal.avg()
  >>> 3.0
  cal2 = Calculator([6, 7, 8, 9, 10])
  cal2.sum()
  >>> 40
  cal2.avg()
  >>> 8.0
"""
# import statistics

# class Calculator:
#   def __init__(self, li):
#     self.li = li
#   def sum(self):
#     return sum(self.li)
#   def avg(self):
#     return statistics.mean(self.li)

# cal1 = Calculator([1, 2, 3, 4, 5])
# print(cal1.sum())
# print(cal1.avg())
# cal2 = Calculator([6, 7, 8, 9, 10])
# print(cal2.sum())
# print(cal2.avg())

"""
Q11. 모듈 사용 방법
  C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.
  (즉 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다.)
  import mymod
"""
# from mymod import *

"""
Q12. 오류와 예외 처리
  다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.
  - 맨 처음 오류인 IndexError와 finally 두 가지
  result = 0
  try:
    [1, 2, 3][3]
    'a' + 1
    4 / 0
  except TypeError:
    result += 1
  except ZeroDivisionError:
    result += 2
  except IndexError:
    result += 3
  finally:
    result += 4

  print(result)
"""
# result = 0
# try:
#   [1, 2, 3][3]
#   'a' + 1
#   4 / 0
# except TypeError:
#   result += 1
# except ZeroDivisionError:
#   result += 2
# except IndexError:
#   result += 3
# finally:
#   result += 4

# print(result)

"""
Q13. DashInsert 함수
  DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 -를 추가하고, 짝수가 연속되면 *를 추가하는 기능을 갖고 있다.
  DashInsert 함수를 완성하시오.
  입력 예시: 4546793
  출력 예시: 454*67-9-3
"""
# string = '4546793'
# string = list(map(int, string))
# newString = ''

# for i, num in enumerate(string):
#   if i == 0:
#     newString += str(num)
#   else:
#     if string[i - 1] % 2 == 1 and num % 2 == 1:
#       newString += '-' + str(num)
#     elif string[i - 1] % 2 == 0 and num % 2 == 0:
#       newString += '*' + str(num)
#     else:
#       newString += str(num)

# print(newString)

"""
Q14. 문자열 압축하기
  문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.
  입력 예시: aaabbcccccca
  출력 예시: a3b2c6a1
"""
# txt = 'aaabbcccccca'
# string = txt[0]
# currentChr = ''
# currentCnt = 1
# for i, chr in enumerate(txt):
#   if chr != currentChr:
#     currentChr = chr
#     string += str(currentCnt)
#     string += chr
#     currentCnt = 1
#   elif chr == currentChr:
#     currentCnt += 1

# string += str(currentCnt)
# print(string)

"""
Q15. Duplicate Numbers
  0 ~ 9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0 ~ 9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
  입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
  출력 예시: True False False True False
"""
# txt = '0123456789 01234 01234567890 6789012345 012322456789'
# li = txt.split(' ')
# for string in li:
#   for i in range(0, 10):
#     tempString = string.replace(str(i), '', 1)
#     if(string == tempString):
#       string = str(i)
#       break
#     else:
#       string = tempString

#   if string == '':
#     print(True)
#   else:
#     print(False)


"""
Q16. 모스 부호 해독
  문자열 형식으로 입력받은 모스 부호(dot: . , dash: -)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오
    - 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
    - 예를 들어 다음 모스 부호는 'HE SLEEPS EARLY'로 해석해야 한다.
    .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
"""
# string = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
# result = ''
# mos = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
#         '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',}
# li = string.split('  ')
# for word in li:
#   mosLi = word.split(' ')
#   for innerMos in mosLi:
#     result += mos[innerMos]
#   result += ' '
# print(result)

"""
Q17. 기초 메타 문자
  다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
  1. acccb
  2. a...b V
  3. aaab
  4. a.cccb
"""
# import re
# p = re.compile('a[.]{3,}b')
# li = ['acccb', 'a...b', 'aaab', 'a.cccb']
# for txt in li:
#   m = p.match(txt)
#   if m:
#     print(m.group())

""" *
Q18. 문자열 검색
  다음 코드의 결괏값은 무엇일까?
"""
# import re
# p = re.compile('[a-z]+')
# m = p.search('5 python')
# print(m.start() + m.end())

"""
Q19. 그루핑
  다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.
"""
# import re

# txt = """
# park 010-9999-9998
# kim 010-9909-7789
# lee 010-8789-7768
# """

# p = re.compile('(\d{3}[-]\d{4})[-]\d{4}')
# result = p.sub('\g<1>-####', txt)
# print(result)

"""
Q20. 전방 탐색
  다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다. 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌
  이메일 주소는 제외시키는 정규식을 작성하시오.
  .*[@].*[.].*$
"""
# import re

# p = re.compile('.*[@].*[.](?=com$|net$).*$')

# print(p.match('pahkey@gmail.com'))
# print(p.match('kim@daum.net'))
# print(p.match('lee@myhome.co.kr'))
