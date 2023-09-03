#!/usr/bin/python3
def x(list):
  a = 0  
  for num in list:
    if num == 4:
      a = a + 1
  return a

print(x([1, 4, 6, 4, 4, 7, 4]))
