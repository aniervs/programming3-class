with open("txt/gear.txt") as f:
    l = [line.strip() for line in f]

r = 0

m, n = len(l), len(l[0])

ct = [[0] * n for _ in range(m)]
pd = [[1] * n for _ in range(m)]

for i in range(m):
    j = 0
    
    while j < n:
        c = 1
        
        while j < n - 1 and l[i][j].isdigit() == l[i][j + 1].isdigit():
            c += 1
            j += 1
            
        if l[i][j].isdigit():
            num = int(l[i][j-c+1:j+1])
            v = False
            
            for x in range(i - 1, i + 2):
                for y in range(j - c, j + 2):
                    if 0 <= x < m and 0 <= y < n and l[x][y] != "." and not l[x][y].isdigit():
                        v = True
                        
                    if 0 <= x < m and 0 <= y < n and l[x][y] == "*":
                        ct[x][y] += 1
                        pd[x][y] *= num
                        break
                    
            if v:
                r += num
                
        j += 1

rt = 0

for i in range(m):
    for j in range(n):
        if ct[i][j] == 2:
            rt += pd[i][j]

print(rt)
