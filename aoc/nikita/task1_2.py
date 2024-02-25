f = open('texts/task1', 'r')
sp = []

line = f.readline()
while line != '':
    sp.append(line)
    line = f.readline()
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num = []
for word in range(len(sp)):
    first_n = True
    last_n = True
    n = ''
    for let in range(len(sp[word])):
        if len(n) == 1:
            break
        if sp[word][let].isdigit() and first_n:
            n += sp[word][let]
            first_n = False
            break
        for cl in numbers:
            if sp[word][let:let+len(cl)] == cl:
                n += f'{numbers.index(cl)+1}'
                break
    for let in range(len(sp[word])):
        if len(n) == 2:
            break
        if sp[word][len(sp[word]) - let - 1].isdigit() and last_n:
            n += sp[word][len(sp[word]) - let - 1]
            last_n = False
            break
        for cl in numbers:
            if sp[word][len(sp[word])-let-len(cl):len(sp[word])-let] == cl:
                n += f'{numbers.index(cl)+1}'
                break
    num.append(int(n))
    print(int(n))
print(sum(num))
