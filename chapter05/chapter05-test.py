"""
Q1. 다음은 Calculator 클래스이다.

  class Calculator:
    def __init__(self):
      self.value = 0
    
    def add(self, val):
      self.value += val

  위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자. 
  즉 다음과 같이 동작하는 클래스를 만들어야 한다.
  cal = UpgradeCalculator()
  cal.add(10)
  cal.minus(7)

  print(cal.value)
"""
# class Calculator:
#   def __init__(self):
#     self.value = 0
  
#   def add(self, val):
#     self.value += val

# class UpgradeCalculator(Calculator):
#   def minus(self, val):
#     self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

"""
Q2. 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어보자. 
    즉 다음과 같이 동작해야 한다.

    cal = MaxLimitCalculator()
    cal.add(50)
    cal.add(60)

    print(cal.value)
"""
# class Calculator:
#   def __init__(self):
#     self.value = 0

#   def add(self, val):
#     self.value += val

# class MaxLimitCalculator(Calculator):
#   def add(self, val):
#     if self.value + val > 100:
#       self.value = 100
#     else:
#       self.value += val

# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)

"""
Q3. 다음 결과를 예측해보자.
  - all([1, 2, abs(-3)-3]) => False
  - chr(ord('a')) == 'a' => True
"""
# print(all([1, 2, abs(-3)-3]))
# print(chr(ord('a')) == 'a')

"""
Q4. filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
"""
# print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

"""
Q5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
  hex(234)
  '0xea'
  이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해보자.
"""
# hexNum = '0xea'
# print(int(hexNum, 16))

"""
Q6. map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
"""
# print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

"""
Q7. 다음 리스트의 최댓값과 최솟값의 합을 구해보자.
  [-8, 2, 7, 5, -3, 5, 0, 1]
"""
# tempList = [-8, 2, 7, 5, -3, 5, 0, 1]
# maxValue = max(tempList)
# minValue = min(tempList)
# print(maxValue + minValue)

"""
Q8. 17 / 3의 결과는 다음과 같다.
  17 / 3
  5.666666666667
  위와 같은 결괏값 5.666666666667을 소숫점 4자리까지만 반올림하여 표시해보자.
"""
# print(round(17 / 3, 4))

"""
Q9. 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해보자.
"""
# from modules.question9 import *

"""
Q10. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해보자.
  1. C:\doin 디렉터리로 이동한다.
  2. dir 명령을 실행하고 그 결과를 변수에 담는다.
  3. dir 명령의 결과를 출력한다.
"""
# import os

# os.chdir('chapter05/modules')

# result = os.popen('dir')
# print(result.read())

"""
Q11. glob 모듈을 사용하여 c:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
"""
# import glob

# print(glob.glob('chapter05/*.py'))

"""
Q12. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.
  2018/04/03 17:20:32
"""
# import time

# print(time.strftime('%x %X', time.localtime(time.time())))

"""
Q13. random 모듈을 사용하여 로또 번호 (1, 45사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안됨)
"""
# import random

# numList = list(range(1, 46))
# choiceList = []
# for i in range(0, 6):
#   choiceNum = random.choice(numList)
#   numList.remove(choiceNum)
#   choiceList.append(choiceNum)
  
# choiceList.sort()
# print(choiceList)
