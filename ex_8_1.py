fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x = line.split()
    for i in range(len(x)):
        if not x[i] in lst:
            lst.append(x[i])
lst.sort()
print(lst)
