"""
05-6. 외장 함수
"""

"""
sys: 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
"""
# import sys
# print(sys.argv)

# 강제로 스크립트 종료
# sys.exit()

# print(sys.path)

"""
pickle: 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
"""
# import pickle

# f = open('storage/test.txt', 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()

# f = open('storage/test.txt', 'rb')
# data = pickle.load(f)
# print(data)

"""
os: 환경 변수나 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해주는 모듈이다.
  - os.environ: 현재 시스템의 환경 변수 값을 알고 싶을 때
"""
# import os
# print(os.environ)
# print(os.environ['PATH'])

# 현재의 위치 돌려받기
# print(os.getcwd())

# os.system: 시스템 명령어 호출하기
# os.system('ls -al')

# os.popen: 실행한 시스템 명령어의 결괏값 돌려받기
# f = os.popen('pwd')
# print(f.read())

"""
기타 유용한 os관련 함수
os.mkdir(dir): 디렉터리를 생성한다.
os.rmdir(dir): 디렉터리를 삭제한다(비어있어야 가능)
os.unlink(fileName): 파일을 지운다
os.rename(fileName, changeFileName): fileName라는 이름의 파일을 changeFileName라는 이름으로 바꾼다.
"""

"""
shutil: 파일을 복사해 주는 파이썬 모듈이다.
"""
# import shutil

# shutil.copy('storage/test.txt', 'storage/text.txt')

"""
glob: 특정 디렉터리에 있는 파일 이름을 모두 보여준다.
"""
# import glob
# print(glob.glob('storage/*'))

"""
tempfile: 파일을 임시로 만들어서 사용할 때 사용
"""
# import tempfile

# filename = tempfile.mktemp()
# print(filename)

"""
time: 시간과 관련된 함수
  - 시간표기: p254참고
"""
# import time

# print(time.time())
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))
# print(time.ctime())

# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# print(time.strftime('%x', time.localtime(time.time())))
# print(time.strftime('%c', time.localtime(time.time())))

# sleep: 일정한 시간 간격을 두고 루프를 실행
# for i in range(1, 11):
#   print(i)
#   time.sleep(1)

# calendar: 달력 출력 모듈
# import calendar

# print(calendar.calendar(2015))
# calendar.prcal(2015)
# calendar.prmonth(2015, 12)

# 해당 날짜의 요일 => 0: 월 / 1: 화 / 2: 수 / 3: 목 / 4: 금 / 5: 토 / 6: 일
# print(calendar.weekday(2015, 12, 31))

# monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
# print(calendar.monthrange(2022, 2))

"""
random: 난수를 발생시키는 모듈이다.
"""
# import random

# print(random.random())
# print(random.randint(1, 10))
# print(random.randint(1, 55))

# data = [1, 2, 3, 4, 5]

# def randomPop(data):
#   number = random.choice(data)
#   data.remove(number)
#   return number

# random.shuffle: 리스트의 항목을 무작위로 섞고 싶을 때 사용
# data = [1, 2, 3, 4, 5]
# random.shuffle(data)
# print(data)

"""
webbrowser: 기본 웹 브라우저를 자동으로 실행하는 모듈
  - open: 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동한다.
  - open_new: 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.
"""
# import webbrowser

# webbrowser.open('http://google.com')
# webbrowser.open_new('http://google.com')

"""
threading 사용
  - Thread(target=): 스레드를 생성한다.
  - start(): 스레드를 실행한다.
  - join(): 스레드가 종료될 때까지 기다린다.
"""
# import time
# import threading

# def longTask():
#   for i in range(5):
#     time.sleep(1)
#     print(f'working:{i}\n')

# print('Start')

# threads = []
# for i in range(5):
#   t = threading.Thread(target = longTask)
#   threads.append(t)

# for t in threads:
#   t.start()

# for t in threads:
#   t.join()

# print('End')