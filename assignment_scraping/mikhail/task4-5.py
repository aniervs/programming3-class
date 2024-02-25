def limit(input_generator, max_count):
    """
    Generator that returns not more than max_count values from the input_generator.

    Args:
    - input_generator: The generator to fetch values from.
    - max_count (int): The maximum number of values to yield.

    Yields:
    - Values from the input_generator, up to max_count values.
    """
    count = 0
    for value in input_generator:
        if count < max_count:
            yield value
            count += 1
        else:
            break

def my_generator():
    for i in range(10): 
        yield i

limited_values = limit(my_generator(), 5)

for value in limited_values:
    print(value)
