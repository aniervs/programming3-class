file_path = "files/task1"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
sum = 0

def check_rev(i,j):
    if arr[i][j].isdigit():
        return int(arr[i][j])

    return 0

def check(i,j):
    if arr[i][j].isdigit():
        return int(arr[i][j])
    return 0

for i in range(len(arr)):
    k = 0
    j = len(arr[i])-1
    f = True
    l = True
    strsum=''
    while (k < len(arr[i]) != 0):
        if(check(i,k)):
            strsum += str(check(i,k))
            break
        k+=1
    while (j >=0):
        if(check_rev(i,j) != 0):
            strsum += str(check_rev(i,j))
            break
        j-=1
    sum += int(strsum)
print(sum)