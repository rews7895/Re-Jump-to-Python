"""
Q1. 다음 코드의 결괏갓은 무엇일까?
  - shirt
"""
# a = 'Life is too short, you need python'

# if 'wife' in a: print('wife')
# elif 'python' in a and 'you' not in a: print('python')
# elif 'shirt' not in a: print('shirt')
# elif 'need' in a: print('need')
# else: print('none')

"""
Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
"""
# result = 0
# i = 1
# while i <= 1000:
#   if i % 3 == 0:
#     result += i
#   i += 1

# print(result)

"""
Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
"""
# i = 0
# while True:
#   i += 1
#   if i > 5: break
#   print('*' * i)

"""
Q4. for문을 사용해 1부터 100까지의 숫자를 출력해보자
"""
# for i in range(1, 101):
#   print(i)

"""
Q5. A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
  [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
  for문을 사용하여 A학급의 평균 점수를 구해보자
"""
# a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in a:
#   total += score

# average = total / len(a)

# if average % 1 == 0:
#   average = round(average)
# else: 
#   average = round(average, 2)

# print(average)

"""
Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
  number = [1, 2, 3, 4, 5]

  result = []
  for n in numbers:
    if n % 2 == 1:
      result.append(n * 2)
"""
# number = [1, 2, 3, 4, 5]
# result = [n * 2 for n in number if n % 2 == 1]
# print(result)