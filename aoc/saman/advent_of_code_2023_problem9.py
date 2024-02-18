# part 1
"""
file=open("problem9.txt","r")
lines=file.readlines() 
def check(a:list)->int:
    test=0
    for i in range(0,len(a)):
        if (a[i]!=0):
            test=1
    if (test==0):
        return 0
    for i in range(0,len(a)-1):
        a[i]=a[i+1]-a[i]
    x=a[len(a)-1]
    del a[len(a)-1]
    return  check(a)+x
sum=0
for i in range(len(lines)):
    ll=lines[i].strip().split(' ')
    for i in range(len(ll)):
        ll[i]=int(ll[i])
    sum+=check(ll)
print(sum)
""" 
#part 2
file=open("problem9.txt","r")
lines=file.readlines() 
def check(a:list)->int:
    test=0
    for i in range(0,len(a)):
        if (a[i]!=0):
            test=1
    if (test==0):
        return 0
    x=a[len(a)-1]
    for i in range(0,len(a)-1):
        a[i]=a[i]-a[i+1]
    del a[len(a)-1]
    return  x-check(a)
sum=0
for i in range(len(lines)):
    ll=lines[i].strip().split(' ')
    for i in range(len(ll)):
        ll[i]=int(ll[i])
    ll.reverse()
    sum+=check(ll)
print(sum)