import heapq

def merge_sorter(*args):
    """
    Generator that merges multiple sorted sequences of integers into a single sorted sequence.

    Args:
    - *args: An arbitrary number of iterables, each containing a sequence of integers sorted in non-decreasing order.

    Yields:
    - Integers from the input sequences, sorted in non-decreasing order.
    """
    min_heap = []

    def start_iterables(args):
        for it_num, iterable in enumerate(args):
            iterator = iter(iterable)
            try:
                first_item = next(iterator)
                heapq.heappush(min_heap, (first_item, it_num, iterator))
            except StopIteration:
                pass

    start_iterables(args)

    while min_heap:
        value, it_num, iterator = heapq.heappop(min_heap)
        yield value
        try:
            next_value = next(iterator)
            heapq.heappush(min_heap, (next_value, it_num, iterator))
        except StopIteration:
            pass

# Example usage
# Merging sorted sequences
sorted_seq1 = [1, 5, 9]
sorted_seq2 = [2, 6, 10]
sorted_seq3 = [3, 4, 7, 8]

merged = merge_sorter(sorted_seq1, sorted_seq2, sorted_seq3)
for number in merged:
    print(number, end=' ')
