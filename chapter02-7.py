# 02-7 불 자료형

a = True
b = False

print(type(a))

print(1 == 1)

a = [1, 2, 3, 4]
while a:
  print(a.pop())

if [1, 2, 3]:
  print('참')
else:
  print('거짓')

print(bool('python'))
print(bool(''))

print(bool([1, 2, 3]))
print(bool([]))

# 0이외의 수는 모두 True
print(bool(0))
print(bool(-1))
print(bool(3))