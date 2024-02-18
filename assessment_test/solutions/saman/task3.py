a=input()
a=a.split(' ')
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
a.append('*')
l=1
l=int(l)
for i in range(len(a)-1):
    if (a[i]!=a[i+1]):
        if (l>=2):
            print(a[i],end=" ")
            l=1
    else :
        l+=1

        
