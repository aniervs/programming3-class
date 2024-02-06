def find_duplicates(arr):
    ans = []
    mp = {}
    for i in arr:
        mp[i] = 0
    for i in arr:
        mp[i] += 1

    for key in mp:
        if mp[key] > 1:
            ans.append(key)    
    return ans

arr = [1, 2, 1, 2, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]

print(find_duplicates(arr))
print(find_duplicates(arr2))