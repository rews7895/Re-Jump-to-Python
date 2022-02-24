# 02-2. 문자열 자료형

a = "Hello world"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python'''
e = "Python\'s fun"

# print(e)

f = "\"Python is very easy.\" he says."
# print(f)

g = "aaa\nbbb"
# print(g)

multiline = '''
  Life is to short
  You need python
'''

# print(multiline)

head = "Python"
tail = " is fun!"

# print(head + tail)

string = 'Python'
# print(string * 2)

# print("=" * 50)
# print("My Program")
# print("=" * 50)

txt = "Life is too short"
# print(len(txt))

date = "2022-02-20 18:23:59"

# print(date[4])
# print(date[0:10])
# print(date[0] + date[1] + date[2] + date[3])
# print(date[:10])
# print(date[11:])

txt = "치킨 가격은 %d원 입니다." %19000
# print(txt)

txt = "배달 시킨 치킨은 %s입니다." %"BBQ"
# print(txt)

cEa = 3
txt = "치킨은 총 %d마리 배달시켰습니다." %cEa
# print(txt)

txt = "치킨을 총 %d%%먹었습니다." %90
# print(txt)

txt = "%0.2f" %3.141592
# print(txt)

txt = "I eat {0} apples".format(3)
# print(txt)

number = 3
txt = "I eat {0} apples".format(number)
# print(txt)

number = 10
day = "three"
txt = "i ate {0} apples. so I was sick for {1} days.".format(number, day)
# print(txt)

txt = "{0:<10}".format("hi")
# print(txt + 'a')

txt = "{0:>10}".format("hi")
# print(txt)

#가운데 정렬
txt = "{0:^10}".format("hi")
# print(txt)

txt = "{0:=^10}".format("Hi")
# print(txt)

y = 3.42134234
txt = "{0:0.4f}".format(y)
# print(txt)

#문자열 포멧팅
name = "홍길동"
age = 31
txt = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# print(txt)

age = 30
txt = f'나는 내년이면 {age + 1}살이 된다.'
# print(txt)

txt = f'{"hi":=^10}'
# print(txt)

txt = f'{"python":!^12}'
# print(txt)

#문자 개수 세기
a = "apple"
# print(a.count('p'))
# print(len(a))

#위치
a = "Python is the best choice"
# print(a.find('b'))
# print(a.find('k'))

# print(",".join('abcd'))

a = "Life is too short"
# print(a.index('t'))
# # print(a.index('k'))

a = "apple"
# print(a.upper())

a = "HI"
# print(a.lower())

a = " hi "
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())

a = "Life is too short"
# print(a.replace("Life", "Your Leg"))
# print(a.split())

b = "a:b:c:d"
# print(b.split(":"))