name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
            zero = line.find(':')
            number = line[zero-3:zero]
            counts[number] = counts.get(number, 0) + 1
            continue
first = list()
for a,b in counts.items():
    x = (a,b)
    first.append(x)
first = sorted(first)
for a,b in first:
    print(a,b)
