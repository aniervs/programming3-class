# time = [7, 15, 30]
# distance = [9, 40, 200]
time = [35, 69, 68, 87]
distance = [213, 1168, 1086, 1248]

n = len(time)
ans = []
for i in range(n):
    cur = 0
    for speed in range(time[i]):
        time_left = time[i] - speed
        my_distance = speed * time_left
        if my_distance > distance[i]:
            cur += 1
    ans.append(cur)

res = 1
for x in ans:
    res *= x
print(res)
