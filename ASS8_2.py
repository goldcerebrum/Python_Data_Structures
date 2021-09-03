fname = input("Enter file name: ")
fh = open(fname)
first = []
for line in fh:
    fline = line.split()
    for x in fline:
        if x not in first:
            first.append(x)
        continue
first.sort()
print(first)
