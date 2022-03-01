"""
06-3. 게시판 페이징하기
  - m: 총 게시물 건수 / n: 한 페이지에 보여줄 게시물 수
"""
def getTotalPage(m, n):
  if m % n == 0:
    return m // n
  else:
    return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(10, 10))
print(getTotalPage(15, 10))
print(getTotalPage(20, 10))
print(getTotalPage(25, 10))

