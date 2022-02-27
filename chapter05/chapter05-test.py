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

