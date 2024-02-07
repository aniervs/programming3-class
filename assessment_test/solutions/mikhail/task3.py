def findDuplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(findDuplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 7]))
