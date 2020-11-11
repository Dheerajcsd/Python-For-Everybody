name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = list()
counts = dict()
for line in handle:
    if line.startswith('From'):
        line.rstrip()
        a = line.split()
        words.append(a[1])
for word in words:
    counts[word] = counts.get(word,0) + 1


maxvalue = -1
maxkey = None
for key,value in counts.items():
    if value > maxvalue:
        maxkey = key
        maxvalue = value

print(maxkey,int(maxvalue/2))

        
