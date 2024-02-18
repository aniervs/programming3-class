file_path = "files/task1"
spell = {'one':1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
sum = 0

def check_rev(i,j):
    if arr[i][j].isdigit():
        return int(arr[i][j])
    if (j - 2 >= 0 and arr[i][j-2:j+1] in spell.keys()):
        return spell[arr[i][j-2:j+1]]
    if (j - 4 >= 0 and arr[i][j - 4:j+1] in spell.keys()):
        return spell[arr[i][j-4:j+1]]
    if (j - 3 >= 0 and arr[i][j - 3:j+1] in spell.keys()):
        return spell[arr[i][j-3:j+1]]

    return 0

def check(i,j):
    if arr[i][j].isdigit():
        return int(arr[i][j])
    if j + 4 < len(arr[i]) and arr[i][j:j + 4] in spell.keys():
        return spell[arr[i][j:j + 4]]
    if j + 3 < len(arr[i]) and arr[i][j:j + 3] in spell.keys():
        return spell[arr[i][j:j + 3]]
    if j+5 < len(arr[i]) and arr[i][j:j + 5] in spell.keys():
        return spell[arr[i][j:j + 5]]
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