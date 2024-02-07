def merge_sorter(*args):
    """
        heapq.merge can merge multiple sorted inputs no matter what the input type is
    """

    from heapq import merge

    return merge(*args)


sorted_list1 = [1, 3, 5]
sorted_list2 = [2, 4, 6]
sorted_generator = (x for x in range(7, 10))  # 7, 8, 9

merged_sequence = merge_sorter(sorted_list1, sorted_list2, sorted_generator)

merged_list = list(merged_sequence)
print(merged_list)
