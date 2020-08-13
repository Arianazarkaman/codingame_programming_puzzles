import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_type = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_type[ext.lower()] = mt
    
for i in range(q):
    fname = input()  # One file name per line.
    
    if not "." in fname:
        print("UNKNOWN")
        continue
    file_ext = fname.split(".")[-1].lower()
    if(mime_type.get(file_ext)):
        print(mime_type[file_ext])
    else:
        print("UNKNOWN")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

