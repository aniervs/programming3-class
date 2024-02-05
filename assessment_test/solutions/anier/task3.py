def find_duplicates(lst):
    marked = set()
    result = set()
    for i in lst:
        if i in marked:
            result.add(i)
        marked.add(i)
    return result 

assert find_duplicates([1,2,3,4,5,6,7,8,9]) == set()
assert find_duplicates([1,1,1,1,1,1,1,1,1]) == {1}
assert find_duplicates([1, 2, 3, 1, 2, 1, 5, 4]) == {1, 2}