def limit(input_generator, max_count):
    """
    Generator that returns not more than max_count values from the input_generator.

    Parameters:
    input_generator (generator): The input generator from which values are taken.
    max_count (int): The maximum number of values to return.

    Yields:
    Values from the input generator, up to a maximum of max_count values.
    """
    count = 0
    for item in input_generator:
        if count < max_count:
            yield item
            count += 1
        else:
            break

# Example of how to use this function:
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

limited_gen = limit(count_up_to(10), 5)
for num in limited_gen:
    print(num)
