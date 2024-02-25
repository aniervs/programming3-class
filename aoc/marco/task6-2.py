# time = 71530
# distance = 940200
time = 35696887
distance = 213116810861248

ans = 0
cur = 0
for speed in range(time):
    time_left = time - speed
    my_distance = speed * time_left
    if my_distance > distance:
        ans += 1
print(ans)
