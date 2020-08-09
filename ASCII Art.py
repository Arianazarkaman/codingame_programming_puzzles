import sys
import math
import string
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input().upper()
letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

for i in range(h):
    row = input()
    
    answer_list = ""
    for letter in t:
        index = letter_list.find(letter)
        if index == -1:
            index = letter_list.find("?")    
        start_l = index * l

        answer_list += row[start_l:start_l+l]
    print(answer_list)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


