fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
            line = line.split()
            word = line[1]
            counts[word] = counts.get(word, 0) + 1
            continue
t = None
s = None
for word,count in counts.items():
    if t is None or count > t:
        s = word
        t = count

print(s, t)
