"""
05-1. 클래스
"""
# class Calculator:
#   def __init__(self):
#       self.result = 0
    
#   #더하기
#   def add(self, num):
#     self.result += num
#     return self.result

#   # 빼기
#   def sub(self, num):
#     self.result -= num
#     return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

class FourCal:
  # 생성자(Constructor): 객체가 생성될 때 자동으로 호출되는 메서드(초깃값을 설정해야 할 필요가 있을 때 생성자를 구현하는 것이 안전한 방법.)
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def setData(self, first, second):
    self.first = first
    self.second = second

  def add(self):
    result = self.first + self.second
    return result

  def mul(self):
    result = self.first * self.second
    return result
  
  def sub(self):
    result = self.first - self.second
    return result

  def div(self):
    result = self.first / self.second
    return result

# a = FourCal()
# print(type(a))
# a.setData(4, 2)
# print(a.first)
# print(a.second)

# b = FourCal()

# a.setData(4, 2)
# print(a.first)
# b.setData(3, 7)
# print(b.first)

# a.setData(4, 2)
# print(a.add())

# a.setData(4, 2)
# b.setData(3, 8)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# a = FourCal(4, 2)
# print(a.first)
# print(a.second)
# print(a.add())
# print(a.div())

"""
클래스의 상속(Inheritance)
  - 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것.
  - class 클래스이름(상속할 클래스 이름):
  - 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
"""
class MoreFourCal(FourCal):
  def pow(self):
    result = self.first ** self.second
    return result
  """
  메서드 오버라이딩
    - 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다.
  """
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second

# a = MoreFourCal(4, 0)
# print(a.add())
# print(a.pow())
# print(a.div())

"""
클래스 변수
  - 클래스 변수는 클래스로 만든 모든 객체에 공유된다.
"""
class Family:
  lastName = '김'

# print(Family.lastName)
# Family.lastName = '박'
# print(Family.lastName)