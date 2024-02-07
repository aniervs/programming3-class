#part one
file=open("problem4.txt","r")
lines=file.readlines()
sum=0
for line in lines:
    line=line.strip()
    n=line[7:].split('|')
    n[0]=n[0].split(' ')
    n[1]=n[1].split(' ')
    h=.5
    for el in n[1]:
        for le in n[0]:
            if (el.isnumeric() and el==le):
                h*=2
                break
    if (h>=1):
        sum+=h
print(sum)
#part 2
file=open("problem4.txt","r")
lines=file.readlines()
sum=0
count =600*[1]
for i in range(0,len(lines)):
    lines[i]=lines[i].strip()
    n=lines[i][7:].split('|')
    n[0]=n[0].split(' ')
    n[1]=n[1].split(' ')
    h=0
    for el in n[1]:
        for le in n[0]:
            if (el.isnumeric() and el==le):
                h+=1
                break
    if (h>=1):
        for j in range(i+1,i+h+1):
            count[j]+=count[i]
    sum+=count[i]
print(sum)  
        