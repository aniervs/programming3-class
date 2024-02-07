#part 1 
file=open("problem3.txt","r")
lines2=file.readlines()
t="...."  
lines=[[] for _ in range(1000)]
ind=1
lines[0]=['.' for _ in range(200)] 
for i in range(len(lines2)):
    lines2[i]=lines2[i].strip()
    lines[ind]=str(lines2[i])
    x=t+lines[ind]+t
    lines[ind]=x
    ind+=1
lines[ind]=['.' for _ in range(200)]
whole_number=int(0) 
is_symbol=0
sum=int(0)
for i in range (1,ind):
    for j in range(1,len(lines[2])-1):
        if (lines[i][j].isnumeric()):
            if(lines[i][j-1].isnumeric()):
                whole_number*=10
                whole_number+=int(lines[i][j])
            else :
                whole_number=int(lines[i][j])
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if ((not lines[ii][jj].isnumeric()) and(lines[ii][jj]!='.')):
                        is_symbol=1
        else :
            if (lines[i][j-1].isnumeric()):
                if (is_symbol==1):
                    sum+=int(whole_number)
            whole_number=0    
            is_symbol=0           
print(sum)
#part 2
file=open("problem3.txt","r")
lines2=file.readlines()
t="...."  
lines=[[] for _ in range(1000)]
ind=1
lines[0]=['.' for _ in range(200)] 
for i in range(len(lines2)):
    lines2[i]=lines2[i].strip()
    lines[ind]=str(lines2[i])
    x=t+lines[ind]+t
    lines[ind]=x
    ind+=1
lines[ind]=['.' for _ in range(200)]
whole_number=int(0) 
is_symbol=0
sum=int(0)
is_star=[]
stars=[[ [] for _ in range(len(lines[2])+1)] for _ in range(ind+1)]
for i in range (1,ind):
    for j in range(1,len(lines[2])-1):
        if (lines[i][j].isnumeric()):
            if(lines[i][j-1].isnumeric()):
                whole_number*=10
                whole_number+=int(lines[i][j])
            else :
                whole_number=int(lines[i][j])
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if (lines[ii][jj]=='*'):
                        if(not ([ii,jj] in is_star)):
                            is_star.append([ii,jj])
        else :
            if (lines[i][j-1].isnumeric()):
                for k in range(0,len(is_star)):
                     stars[is_star[k][0]][is_star[k][1]].append(whole_number)
            is_star.clear()
            whole_number=0    
for i in range(1,ind):
    for j in range(1,len(lines[2])):
        if (len(stars[i][j])==2):
            sum+=stars[i][j][0]*stars[i][j][1]
print(sum)
                
            
        