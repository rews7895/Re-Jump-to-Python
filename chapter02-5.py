# 02-5 딕셔너리형

jun = {'name': 'jun', 'phone': '01011111111', 'age': 31}
seok = {'name': 'seok', 'phone': '01022222222', 'age': 22}

dataArr = []
dataArr.append(jun)
dataArr.append(seok)

print(dataArr)

a = {1: 'hi'}

a = {'a': [1, 2, 3]}

a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'jun'

print(a)

# 요소 삭제하기
del a[1]
print(a)

dic = {'김연아': '피겨스케이팅', '류현진': '야구', '박지성': '축구', '귀도': '파이썬'}
print(dic['김연아'])

# key값 가져오기
print(dic.keys())

for key in dic.keys():
  print(key)

dicKeyList = list(dic.keys())
print(dicKeyList[0])

# value값 가져오기
dicValList = list(dic.values())
print(dicValList)

# key, value 쌍 얻기
dicItemList = list(dic.items())
print(dicItemList)

for item in dicItemList:
  print(item[0] + ' / ' + item[1])

# key: value쌍 지우기
dic.clear()
print(dic)

dic = {'name': 'jun', 'age': 31, 'job': 'developer'}
print(dic.get('name'))

if dic.get('anme'):
  print('있다')
else:
  print('없다')

dicPractice = {'name': '홍길동', 'birth': '1128', 'age': 30}
print(dicPractice)