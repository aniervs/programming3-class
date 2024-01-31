def find_duplicates(arr):
    seen = set()
    dup_set = set()
    dup = []

    for num in arr:
        if num in seen:
            if num not in dup_set:
                dup.append(num)
                dup_set.add(num)
        else:
            seen.add(num)

    return dup

print(find_duplicates([1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]))