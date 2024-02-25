# part 1 
"""
red_limit=12
blue_limit=14
green_limit=13
dic={'green':0,'blue':0,'red':0}
file=open("problem2_p1.txt","r")
sum=0
lines=file.readlines()
ind=0
for line in lines :
    ind+=1
    dic['green']=0
    dic['red']=0
    dic['blue']=0
    line=line.strip()
    n=line[6:].split(';')
    for np in n:
        k=np.split(' ')
        for i in range(0,len(k)-1):
            if (k[i].isnumeric()):
                k[i]=int(k[i])
                if ((k[i+1]=='green' or k[i+1]=='green,') and dic['green']<k[i]):
                    dic['green']=k[i]
                if ((k[i+1]=='blue'or k[i+1]=='blue,') and dic['blue']<k[i]):
                    dic['blue']=k[i]
                if ((k[i+1]=='red'or k[i+1]=='red,') and dic['red']<k[i]):
                    dic['red']=k[i]
    if (dic['green']<=green_limit and dic['red']<=red_limit and dic['blue']<=blue_limit):
        sum+=ind
print(sum)
"""
#part 2
red_limit=12
blue_limit=14
green_limit=13
dic={'green':0,'blue':0,'red':0}
file=open("problem2_p1.txt","r")
sum=0
lines=file.readlines()
ind=0
for line in lines :
    ind+=1
    dic['green']=0
    dic['red']=0
    dic['blue']=0
    line=line.strip()
    n=line[6:].split(';')
    for np in n:
        k=np.split(' ')
        for i in range(0,len(k)-1):
            if (k[i].isnumeric()):
                k[i]=int(k[i])
                if ((k[i+1]=='green' or k[i+1]=='green,') and dic['green']<k[i]):
                    dic['green']=k[i]
                if ((k[i+1]=='blue'or k[i+1]=='blue,') and dic['blue']<k[i]):
                    dic['blue']=k[i]
                if ((k[i+1]=='red'or k[i+1]=='red,') and dic['red']<k[i]):
                    dic['red']=k[i]
    sum+=dic['green']*dic['blue']*dic['red']
print(sum)
            
        
    
    
      



















 