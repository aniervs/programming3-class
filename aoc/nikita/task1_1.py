f = open('texts/task1', 'r')
sp = []

line = f.readline()
while line != '':
    sp.append(line)
    line = f.readline()

num = []
for word in range(len(sp)):
    first_n = True
    last_n = True
    n = ''
    for let in range(len(sp[word])):
        if sp[word][let].isdigit() and first_n:
            n += sp[word][let]
            first_n = False
    for let in range(len(sp[word])):
        if sp[word][len(sp[word])-let-1].isdigit() and last_n:
            n += sp[word][len(sp[word])-let-1]
            last_n = False
    num.append(int(n))
    print(int(n))
print(sum(num))