def merge(*args):
    """
    Generator that merges sorted sequences of integers.
    """
    iterators = [iter(arg) for arg in args]
    values = [next(iterator) for iterator in iterators]

    while True:
        min_value = min(values)
        yield min_value

        index = values.index(min_value)
        try:
            values[index] = next(iterators[index])

        except StopIteration:
            del values[index]
            del iterators[index]

        if len(values) == 0:
            break

arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
arr3 = [0, 11, 13]


print(list(merge(arr1, arr2, arr3)))
