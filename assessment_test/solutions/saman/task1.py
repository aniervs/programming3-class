n=int(input())
m=int(input())
a=100*[[]]
b=10000*[]
for i in range(0,n):
    a[i]=input()
    a[i]=a[i].split(' ')
    for j in range(m):
        a[i][j]=int(a[i][j])
ind=0
y=-1
x=0
#print(a[1][2])
number=n*m
n-=1
while number>0:
    if (m>0):
        if (ind==0):
            for _ in range(m):
                y+=1
                number-=1
                if (number<0):
                    break
                print(a[x][y],end=" ")
            m-=1
        else :
            for _ in range(m):
                y-=1
                number-=1
                if (number<0):
                    break
                print(a[x][y],end=" ")
            m-=1
    if (n>0):
        if (ind==0):
            for _ in range(n):
                x+=1
                number-=1
                if (number<0):
                    break
                print(a[x][y],end=" ")
            n-=1
        else :
            for _ in range(n):
                x-=1
                number-=1
                if (number<0):
                    break
                print(a[x][y],end=" ")
            n-=1
    ind=1-ind
