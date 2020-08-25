import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
message = input()

res = ''.join('{0:07b}'.format(ord(c))for c in message)
word_binary = str(res)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
last, count = None, 0
for c in word_binary:
    if c != last:
        print(('0' * count) + (' ' if count else '') + ("00 " if c == '0' else "0 "), end='')
        count = 1
    else:
        count+=1
    last = c
print("0" * count, end="")



