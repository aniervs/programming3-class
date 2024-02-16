#part 1 
"""
def check_for_Five_of_a_kind():
    for i in b:
        if (dict[i]==5):
            return 1
    return 0
def check_for_Four_of_a_kind():
    for i in b:
        if (dict[i]==4):
            return 1
    return 0
def check_for_Three_of_a_kind():
    for i in b:
        if (dict[i]==3):
            return 1
    return 0
def check_for_Full_house():
    num2=0
    num3=0
    for i in b:
        if (dict[i]==3):
            num3+=1
        if (dict[i]==2):
            num2+=1
    if (num3==1 and num2==1):
        return 1
    return 0
def check_for_Two_pair():
    num2=0
    for i in b:
        if (dict[i]==2):
            num2+=1
    if (num2==2):
        return 1
    return 0
def check_for_One_pair():
    num2=0
    for i in b:
        if (dict[i]==2):
            num2+=1
    if (num2==1):
        return 1
    return 0
def check_for_High_card():
    return 1
dict={}
b=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
a=[]
file=open("problem7.txt","r")
lines=file.readlines()
for i in range(len(lines)):
    n=lines[i].split(' ')
    value=0
    for i in b:
        dict[i]=0
    n[0]=str(n[0])
    #print(n[0],n[1])
    for l in n[0]:
        dict[l]+=1
    if (check_for_Five_of_a_kind()):
        x=4
        for l in n[0]:
            value+=pow(1001,x)*(b.index(l)+1)
            x-=1    
    elif(check_for_Four_of_a_kind()):
        x=4
        for l in n[0]:
            value+=pow(500,x)*(b.index(l)+1)
            x-=1
    elif(check_for_Full_house()):
        x=4
        for l in n[0]:
            value+=pow(241,x)*(b.index(l)+1)
            x-=1
    elif(check_for_Three_of_a_kind()):
        x=4
        for l in n[0]:
            value+=pow(120,x)*(b.index(l)+1)
            x-=1
    elif(check_for_Two_pair()):
        x=4
        for l in n[0]:
            value+=pow(60,x)*(b.index(l)+1)
            x-=1
    elif(check_for_One_pair()):
        x=4
        for l in n[0]:
            value+=pow(29,x)*(b.index(l)+1)
            x-=1
    else :
        x=4
        for l in n[0]:
            value+=pow(14,x)*(b.index(l)+1)
            x-=1
    a.append([value,int(n[1])])
a.sort()
sum=0
for i in range(len(a)):
    sum+=(i+1)*a[i][1]
print(sum)
    """
# part 2
def check_for_Five_of_a_kind():
    for i in range(1,len(b)):
        if (dict[b[i]]+dict[b[0]]==5):
            return 1
    return 0
def check_for_Four_of_a_kind():
    for i in range(1,len(b)):
        if (dict[b[i]]+dict[b[0]]==4):
            return 1
    return 0
def check_for_Three_of_a_kind():
    for i in range(1,len(b)):
        if (dict[b[i]]+dict[b[0]]==3):
            return 1
    return 0
def check_for_Full_house():
    num=0
    for i in range(1,len(b)):
        if (dict[b[i]]>0):
            num+=1
    if (num<=2):
        return 1
    return 0
def check_for_Two_pair():
    num=0
    for i in range(1,len(b)):
        if (dict[b[i]]>0):
            num+=1
    if (num<=3):
        return 1
    return 0
def check_for_One_pair():
    num2=0
    for i in b:
        if (dict[i]==2):
            num2+=1
    if (num2==1 or dict['J']>0):
        return 1
    return 0
def check_for_High_card():
    return 1
dict={}
b=['J','2','3','4','5','6','7','8','9','T','Q','K','A']
a=[]
file=open("problem7.txt","r")
lines=file.readlines()
for i in range(len(lines)):
    n=lines[i].split(' ')
    value=0
    for i in b:
        dict[i]=0
    n[0]=str(n[0])
    for l in n[0]:
        dict[l]+=1
    if (check_for_Five_of_a_kind()):
        x=4
        for l in n[0]:
            value+=pow(1001,x)*(b.index(l)+1)
            x-=1    
    elif(check_for_Four_of_a_kind()):
        x=4
        for l in n[0]:
            value+=pow(500,x)*(b.index(l)+1)
            x-=1
    elif(check_for_Full_house()):
        x=4
        for l in n[0]:
            value+=pow(241,x)*(b.index(l)+1)
            x-=1
    elif(check_for_Three_of_a_kind()):
        x=4
        for l in n[0]:
            value+=pow(120,x)*(b.index(l)+1)
            x-=1
    elif(check_for_Two_pair()):
        x=4
        for l in n[0]:
            value+=pow(60,x)*(b.index(l)+1)
            x-=1
    elif(check_for_One_pair()):
        x=4
        for l in n[0]:
            value+=pow(29,x)*(b.index(l)+1)
            x-=1
    else :
        x=4
        for l in n[0]:
            value+=pow(14,x)*(b.index(l)+1)
            x-=1
    a.append([value,int(n[1])])
a.sort()
sum=0
for i in range(len(a)):
    sum+=(i+1)*a[i][1]
print(sum)
    