fname = input("Enter file name: ")
count = 0
ans = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x = line.find('.')
    ans = ans + float(line[x-1:])
    count = count + 1
print("Average spam confidence:",ans/count)
