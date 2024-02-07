s=input()
dp=100*[100*[0]]
n=len(s)
l=int(0)
r=int(0)
print(s)
#print(dp[2])
for i in range(0,n):
    dp[i][i]=1
for i in range(0,n-1):
    if (s[i]==s[i+1]):
        dp[i][i+1]=1
       # print(i,end=" ")
size=int(0)
for k in range (2,n-1,2):
    for i in range(0,n-k):
        if s[i]==s[i+k] and dp[i+1][i+k-1]==1:
            dp[i][i+k]=1
            if (int(k)>size):
                size=int(k)
                l=int(i) 
                r=int(i)+int(k)
for k in range (3,n-1,2):
    for i in range(0,n-k):
        if s[i]==s[i+k] and dp[i+1][i+k-1]==1:
            dp[i][i+k]=1
            if (int(k)>size):
                size=int(k)
                l=int(i) 
                r=int(i)+int(k)
           # print("\n")
#print("\n")
l=int(l)
r=int(r)
for i in range(l,r+1):
    print(s[i],end=" ")
