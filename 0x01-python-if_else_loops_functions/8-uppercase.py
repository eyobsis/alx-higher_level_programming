#!/usr/bin/python3
def uppercase(s):
for c in s:
    ascii_val = ord(c)
    if ascii_val >= 97 and ascii_val <= 122:
    uppercase = ascii_val - 32
    print(chr(uppercase), end="")
    else:
        print(c, end="")
print()
