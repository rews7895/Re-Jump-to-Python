"""
05-3. 패키지
  - 패키지란 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
  - __init__.py: 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. python3.3 이후부터는 없어도 인식함.
  - __all__: * 기호를 사용하여 import할 경우 해당 곳에 정의된 모듈만 import 된다.
"""
# import game.sound.echo

# game.sound.echo.echoTest()

# from game.sound import *

# echo.echoTest()

# from game.sound.echo import echoTest
# def renderTest():
#   print('render')
#   echoTest()

# renderTest()


