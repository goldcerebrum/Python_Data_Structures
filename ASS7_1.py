# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
rfh = fh.read()
ufh = rfh.upper()
ufh = ufh.rstrip()
print(ufh)
