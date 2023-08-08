#!/usr/bin/python3
result = ""
for i in range(ord('a'), ord('z') + 1):
    result += "{}".format(chr(i))
print(f"{result}", end='')
