name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
            y = line.split()
            t = y[5]
            h = t[:2]
            counts[h] = counts.get(h, 0) + 1
            continue
first = list()
for a,b in counts.items():
    x = (a,b)
    first.append(x)
first = sorted(first)
for a,b in first:
    print(a,b)
