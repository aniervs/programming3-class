# part 1
""" 
file=open("problem11.txt","r")
lines=file.readlines()
x=[0 for _ in range(0,10000)]
y=[0 for _ in range(0,10000)]
num=0
double_x=[0 for _ in range(0,1000)]
double_y=[0 for _ in range(0,1000)]
for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        if (lines[i][j]=='#'):
            test=1
            y[i+1]+=1
            num+=1
            x[j+1]+=1
            
ansy=0
sumy=0
numY_next=num
numY_per=0
ansx=0
sumx=0
numX_next=num
numX_per=0
for i in range(0,10000):
    ansy+=y[i]*i
for i in range(1,10000):
    ansy-=numY_next
    #ansy+=numY_per
    sumy+=ansy*y[i]
    if (y[i]==0):
        sumy+=numY_next*numY_per
    numY_next-=y[i]
    numY_per+=y[i]
for i in range(0,10000):
    ansx+=x[i]*i
for i in range(1,10000):
    ansx-=numX_next
    sumx+=ansx*x[i]
    if (x[i]==0):
        sumx+=numX_next*numX_per
    numX_next-=x[i]
    numX_per+=x[i]
print(sumx+sumy)
"""
#part 2
file=open("problem11.txt","r")
lines=file.readlines()
x=[0 for _ in range(0,10000)]
y=[0 for _ in range(0,10000)]
num=0
double_x=[0 for _ in range(0,1000)]
double_y=[0 for _ in range(0,1000)]
for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        if (lines[i][j]=='#'):
            test=1
            y[i+1]+=1
            num+=1
            x[j+1]+=1
NumberOfCopy=1000000            
ansy=0
sumy=0
numY_next=num
numY_per=0
ansx=0
sumx=0
numX_next=num
numX_per=0
for i in range(0,10000):
    ansy+=y[i]*i
for i in range(1,10000):
    ansy-=numY_next
    sumy+=ansy*y[i]
    if (y[i]==0):
        sumy+=numY_next*numY_per*(NumberOfCopy-1)
    numY_next-=y[i]
    numY_per+=y[i]
for i in range(0,10000):
    ansx+=x[i]*i
for i in range(1,10000):
    ansx-=numX_next
    sumx+=ansx*x[i]
    if (x[i]==0):
        sumx+=numX_next*numX_per*(NumberOfCopy-1)
    numX_next-=x[i]
    numX_per+=x[i]
print(sumx+sumy)
        