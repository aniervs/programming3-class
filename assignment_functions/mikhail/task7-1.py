import heapq

def merge_sorter(*args):
    """
    Generator that merges multiple sorted sequences of integers.

    Parameters:
    *args: An arbitrary number of sorted iterable sequences of integers.

    Yields:
    Integers in non-decreasing order, merged from the input sequences.
    """
    iterators = [iter(seq) for seq in args]

    heap = []
    for index, it in enumerate(iterators):
        first_item = next(it, None)
        if first_item is not None:
            heapq.heappush(heap, (first_item, index))

    while heap:
        smallest, index = heapq.heappop(heap)
        yield smallest

        next_item = next(iterators[index], None)
        if next_item is not None:
            heapq.heappush(heap, (next_item, index))

# Example of how to use this function:
seq1 = [1, 3, 5]
seq2 = [2, 4, 6]
seq3 = [0, 7, 8, 9]
merged = merge_sorter(seq1, seq2, seq3)
for num in merged:
    print(num, end=' ')
