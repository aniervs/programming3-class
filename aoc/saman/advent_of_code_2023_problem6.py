#part 1 
"""
file=open("problem6.txt","r")
n=file.readline().strip()
s=file.readline().strip()
n=n.split(" ")
s=s.split(' ')
sum=1
a=[]
b=[]
for i in range(0,len(n)):
    if (n[i].isnumeric()):
        a.append(int(n[i]))
for i in range(0,len(s)):
    if (s[i].isnumeric()):
        b.append(int(s[i]))
for i in range(0,len(b)):   
        k=a[i]
        kp=b[i]
        mp_1=(k)//2
        mp_2=(k+1)//2
        sum2=0
        while (mp_1*mp_2>kp):
            sum2+=2
            if (mp_1==mp_2):
                sum2-=1
            mp_1-=1
            mp_2+=1
            if(mp_2>=k or mp_1<1):
                break
        sum*=sum2
print(sum)
"""
#part 2
file=open("problem6.txt","r")
n=file.readline().strip()
s=file.readline().strip()
n=n.split(" ")
s=s.split(' ')
sum=0
a=0
b=0
for i in range(0,len(n)):
    if (n[i].isnumeric()):
        a=a*pow(10,len(n[i]))
        a+=int(n[i]) 
for i in range(0,len(s)):
    if (s[i].isnumeric()):
        b=b*pow(10,len(s[i]))
        b+=int(s[i])
print(a,b)   
k=a
kp=b
mp_1=(k)//2
mp_2=(k+1)//2
while (mp_1*mp_2>kp):
    sum+=2
    if (mp_1==mp_2):
        sum-=1
    mp_1-=1
    mp_2+=1
    if(mp_2>=k or mp_1<1):
        break
print(sum)