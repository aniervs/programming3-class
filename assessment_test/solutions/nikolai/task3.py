arr = {}
ans_arr = []
n = int(input("input length of an array:\n"))
for i in range(n):
    key = input()
    if key in arr:
        arr[key] += 1
    else:
        arr[key] = 1

for key in arr:
    if(arr[key] > 1):
        ans_arr.append(key)

print(ans_arr)