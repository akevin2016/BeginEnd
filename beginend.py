# To run:
# python beginend.py <filename>

# Outputs to stdout

import sys

if len(sys.argv) != 2:
    print("Usage: python beginend.py <filename>")
    sys.exit()

f = None
try:
    f = open(sys.argv[1], "r")
except OSError:
    print("File does not exist or could not be opened.")
    sys.exit()

lines = []
order = [0]
for l in f:
    ls = l.strip()
    if ls == "begin":
        order[-1] += 1
        label = " // "
        for n in order:
            label += str(n) + "."
        label = label[:-1]
        l = l.rstrip() + label + "\n"
        order.append(0)

    elif ls == "end":
        order.pop()
        label = " // "
        for n in order:
            label += str(n) + "."
        label = label[:-1]
        l = l.rstrip() + label + "\n"

    lines.append(l)
f.close()

for l in lines:
    print(l, end='')



