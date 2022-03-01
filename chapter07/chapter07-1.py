"""
07-1. 정규 표현식 살펴보기
  - 복잡한 문자열을 처리할 때 사용하는 기법
"""

data = """
park 800905-1049118
kim 700905-1059119
"""

# result =[]
# for line in data.split('\n'):
#   wordResult = []
#   for word in line.split(' '):
#     if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#       word = word[:6] + '-' + '*******'
#     wordResult.append(word)
#   result.append(' '.join(wordResult))
# print('\n'.join(result))

#! 정규식으로 변경하면

# import re

# pat = re.compile('(\d{6})[-]\d{7}')
# print(pat.sub('\g<1>-*******', data))