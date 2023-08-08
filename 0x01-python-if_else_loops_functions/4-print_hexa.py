#!/usr/bin/python3
the_result = ""
for i in range(99):
    the_result += str(i) + " = " + hex(i) + "\n"

print(the_result, end="")
