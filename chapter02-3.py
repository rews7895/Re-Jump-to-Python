odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(c[0])
print(b[0] + b[2])
print(b[-1])

a = [1, 2, 3, 4, 5]
print(a[0: 2])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])

a = [1, 2, 3, 4, 5]
print(a[:2])
print(a[2:])

a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(a * 3)
print(len(a))

# 리스트 값  수정
a = [1, 2, 3]
a[2] = 4
print(a)

# 요소 삭제
del a[2]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a.append(3)
a.append([4, 5])
print(a)
print(a + [4, 5])

arr = [1, 3, 5, 7, 2, 4]
arr.sort()
print(arr)

arr = ['b', 'c', 'd', 'a']
arr.sort()
print(arr)
arr.reverse()
print(arr)

# 위치 반환
arr = ['a', 'b', 'c', 'd']
print(arr.index('c'))

# 요소 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

# 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
a = [1, 2, 3]
a.pop()
print(a)

# x번째 요소를 돌려주고 그 요소를 삭제
a = [1, 2, 3]
a.pop(1)
print(a)

# 값 x의 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)