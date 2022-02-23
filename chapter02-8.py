# 02-8 자료형의 값을 저장하는 공간 변수

a = 1
b = 'python'
c = [1, 2, 3]

# 변수 이름 = 변수에 저장할 값
aId = id(a)
print(f"{aId}주소")

# b배열에 a를 담으면 같은 주소값을 공유하게 되어 a에 변화가 생기면 b에도 변화가 생긴다.
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

a.append(4)
print(a)
print(b)

# a와 b가 가리키는 객체는 동일한가?
print(a is b)

a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
# 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱 -> 다른 주소를 가지게 된다.
b = a[:]
print(id(a))
print(id(b))

a[1] = 4
print(a)
print(b)

from copy import copy

# 리스트를 복사하고 싶을때는 copy모듈을 사용
a = [1, 2, 3]
b = copy(a)
print(a is b)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
# python
print(a)
# life
print(b)

(a, b) = 'python1', 'life2'
# python1
print(a)
# life2
print(b)

[a, b] = ['python', 'life']
# python
print(a)
# life
print(b)

a = b = 'python is good'
print(id(a))
print(id(b))
# True
print(a is b)

# 두 변수의 값을 변경하고 싶을 때!!!!!
a = 3
b = 5
a, b = b, a
print(a)
print(b)

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)
