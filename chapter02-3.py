# 튜플은 리스트와 다르게 ()로 둘러싼다.
# 튜플의 요솟값은 한 번 정하면 지우거나 변경할 수 없다.
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])
print(t1[1:])
t2 = (3, 4)
print(t1 + t2)
print(t2 * 2)
print(len(t2))

t1 = (1, 2, 3)
t2 = (4,)
print(t1 + t2)