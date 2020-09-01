import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
first_y = 0
last_y = h
first_x = 0
last_x = w
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if 'U' in bomb_dir:
        last_y = y0 - 1
    elif 'D' in bomb_dir:
        first_y = y0 + 1
    if 'L' in bomb_dir:
        last_x = x0 - 1
    elif 'R' in bomb_dir:
        first_x = x0 + 1 
    x0 = (first_x + last_x) // 2
    y0 = (first_y + last_y) // 2
    print(x0, y0) 
    # the location of the next window Batman should jump to.

