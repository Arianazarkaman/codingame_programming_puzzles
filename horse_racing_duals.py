import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
strenghts = []
n = int(input())
for i in range(n):
    pi = int(input())
    strenghts.append(int(pi))
# Write an action using print
D = 0 
list = []
strenghts.sort()
for i in range(len(strenghts) - 1):
    D = strenghts[i] - strenghts[i+1]
    Diff = abs(D)
    list.append(Diff)
# To debug: print("Debug messages...", file=sys.stderr)
list.sort()
print(list[0])
