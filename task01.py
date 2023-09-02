#!/usr/bin/python3
list = [18, 52, 23, 41, 32, 99]

ln = list[0]

for x in list:
    if x > ln:
        ln = x

print("Largest element is: ", ln)
