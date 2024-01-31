


# integers_list = [3, 7, 12, 3, 9, 15, 7, 21, 12, 5, 9]
def duplicates(list1):

    new_list = []
    index = 0

    while index < len(list1)-1:
        if list1[index] in list1[index+1:]:
            new_list.append(list1[index])

        index += 1

    return list(set(new_list))

print(duplicates([3, 7, 12, 3, 9, 15, 7, 21, 12, 5, 7, 9]))
