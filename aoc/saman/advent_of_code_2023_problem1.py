#part one 
"""
file=open("C:\\Users\\HP-m03\\Desktop\\class_py\\problem.txt","r")
last_d=0
first_d=0
sum=0
sum=int(0)
while (True):
    n=file.readline()
    if not n:
        break
    for i in range (0,len(n)):
       # n[i]=int(n[i])
        if (n[i].isnumeric()):
            last_d=n[i]
    i=len(n)
    while (i>0):
        i-=1
        if (n[i].isnumeric()):
            first_d=n[i]
    sum+=int(first_d)*10+int(last_d)
print(sum)
"""  
#part two    
file=open("C:\\Users\\HP-m03\\Desktop\\class_py\\problem1_p2.txt","r")
lines=file.readlines()
inf=int(100000)
sum=int(0)
max_ind = len(lines)*[int(-inf)]
max_int = len(lines)*[int(0)]
min_ind = len(lines)*[int(inf)]
min_int = len(lines)*[int(0)]
def check_for_a_number(s:str,num:int):
    global sum
    for j in range (0,len(lines)) :
        for i in range(0,len(lines[j])-len(s)):
            if (s==lines[j][i:i+len(s)]):
                if i>=max_ind[j]:
                    sum-=max_int[j]
                    max_ind[j]=int(i)
                    max_int[j]=num
                    sum+=max_int[j]
        for i in range(len(lines[j])-len(s)-1,-1,-1):
            if (s==lines[j][i:i+len(s)]):
                if (i<=min_ind[j]):
                    sum-=min_int[j]*10
                    min_ind[j]=int(i)
                    min_int[j]=num
                    sum+=min_int[j]*10
check_for_a_number('one',1)
check_for_a_number('two',2)
check_for_a_number('three',3)
check_for_a_number('four',4)
check_for_a_number('five',5)
check_for_a_number('six',6)
check_for_a_number('seven',7)
check_for_a_number('eight',8)
check_for_a_number('nine',9)
for i in range(1,10):
    check_for_a_number(str(i),int(i))
print(sum)