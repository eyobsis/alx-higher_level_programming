#!/usr/bin/python3
output = ''
for i in range(26):
    if i % 2 == 0:
        output += chr(ord('z') - i)
    else:
        output += chr(ord('Z') - i)

print(output, end='')
