"""
04-3 파일 읽고 쓰기
"""
# r: 읽기 모드 / w: 쓰기 모드 / a: 추가 모드 - 파일의 마지막에 새로운 내용을 축다할 때 사용
# f = open('storage/file.txt', 'w')
# f.close()

# f = open('storage/file.txt', 'w')
# for i in range(1, 11):
#   data = f'{i}번째 줄입니다\n'
#   f.write(data)
# f.close()

# 한 줄 출력
# f = open('storage/file.txt', 'r')
# line = f.readline()
# print(line)
# f.close()
  
# 모든 줄 출력
# f = open('storage/file.txt', 'r')

# while True:
#   line = f.readline()
#   if not line: break
#   print(line)

# f.close()

# f = open('storage/file.txt', 'r')
# lines = f.readlines()
# for line in lines:
#   print(line)
# f.close()

# f = open('storage/file.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# 내용 추가 (a)
# f = open('storage/file.txt', 'a')

# for i in range(11, 20):
#   data = f'{i}번째 줄입니다\n'
#   f.write(data)

# f.close()


# f = open('storage/foo.txt', 'w')
# f.write('Life is too short, you need python')
# f.close()

# with문을 이용한 객제 닫기
# with open('storage/foo.txt', 'w') as f:
#   f.write('Life is too short, you need python~!')

# import sys

# args = sys.argv[1:]
# for i in args:
#   print(i.upper(), end='  ')