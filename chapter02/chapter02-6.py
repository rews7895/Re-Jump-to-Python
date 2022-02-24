# 02-6 집합 자료형
#   - 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
#   - 특징으로는
#     1) 중복을 허용하지 않는다.
#     2) 순서가 없다.

s1 = set([1, 2, 3])
# print(s1)

s2 = set('hello')
# print(s2)

# 중복을 제거하기 위한 필터 역할로 종종 사용되기도 한다.
s1 = list(set([1, 4, 3, 2, 2]))
s1.sort()
# print(s1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
# print(s1 & s2)
# print(s1.intersection(s2))

# 합집합
# print(s1 | s2)
# print(s1.union(s2))

# 차집합
# print(s1 - s2)
# print(s2 - s1)

# 1개의 값 추가
s1 = set([1, 2, 3])
s1.add(4)
s1.add(2)
# print(s1)

# 여러개의 값 추가
s1.update([4, 5, 6, 7])
# print(s1)

# 특정값 제거(1개만 가능)
s1.remove(2)
# print(s1)

