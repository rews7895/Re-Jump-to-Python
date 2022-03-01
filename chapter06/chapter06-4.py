"""
06-4. 간단한 메모장 만들기
"""
import sys

option = input()

if option == '-a':
  memo = input()
  f = open('storage/memo.txt', 'a')
  f.write(memo)
  f.write('\n')
  f.close()
elif option == '-v':
  f = open('storage/memo.txt')
  memo = f.read()
  f.close()
  print(memo)