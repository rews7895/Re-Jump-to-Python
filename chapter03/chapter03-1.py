"""
03-1. if문
  - >, <, ==, !=, >=, <= 사용 가능
"""
# money = 2000
# if money >= 3000:
#   print('택시를 타고 간다.')
# else:
#   print('걸어간다.')
  
"""
or / and / not
"""
# money = 2000
# card = True
# if money >= 3000 or card:
#   print('택시를 타고 가라')
# else:
#   print('걸어 가라')

"""
x (not) in (list, tuple, string)
"""
# print(1 in [1, 2, 3])
# print(1 not in [1, 2, 3])

# print('a' in ('a', 'b', 'c'))
# print('j' not in 'python')

"""
elif
"""
# pocket = ['paper','cellphone']
# card = True
# if 'money' in pocket:
#   print('택시를 타고 가라')
# elif card:
#   print('택시를 타고 가라')
# else:
#   print('걸어가라')

"""
간결한 표현식
"""
# pocket = ['paper', 'money', 'cellphone']
# if 'money' in pocket:
#   pass
# else:
#   print('카드를 꺼내라')

# if 'money' in pocket: pass
# else: print('카드를 꺼내라')

"""
조건부 표현식
"""
# score = 40
# if score >= 60:
#   message = 'success'
# else:
#   message = 'failure'

# print(message)

# message = 'success' if score >= 60 else 'failure'
# print(message)