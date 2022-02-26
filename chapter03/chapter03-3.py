"""
03-3.for문
"""
# 전형적인 for 문
# testList = ['one', 'two', 'three']
# for i in testList:
#   print(i)

# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#   print(first + last)

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#   number = number + 1
#   if mark >= 60:
#     print(f'{number}번 학생은 합격입니다.')
#   else:
#     print(f'{number}번 학생은 불합격입니다.')

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#   number = number + 1
#   if mark < 60: continue
#   print(f'{number}번 학생 축하합니다. 합격입니다.')

""" 
  range(): 숫자리스트를 자동으로 만들어준다.
  range(시작, 끝 숫자)
"""
# a = range(10)
# print(a)
# a = range(1, 11)

# add = 0
# for i in range(1, 11):
#   add = add + i
#   print(add)

# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#   if marks[number] < 60: continue
#   print(f'{number + 1}번 학생 축하합니다. 합격입니다.')

# for i in range(2, 10):
#   for j in range(1, 10):
#     print(i * j, end="  ")
#   print('')

# a = [1, 2, 3, 4]
# result = []
# for num in a:
#   result.append(num * 3)

# print(result)

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a]
# print(result)

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

# result = [x * y for x in range(2, 10) for y in range(1, 10)]
# print(result)