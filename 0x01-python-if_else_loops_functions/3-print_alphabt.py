#!/usr/bin/python3
result = " "
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in ['q', 'e']:
        result += chr(i)
print("{}".format(result), end='')
