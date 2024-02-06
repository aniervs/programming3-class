def limit(input_generator, max_count):
    """
    Generator that returns not more than max_count values of the input_generator.
    """
    count = 0
    for value in input_generator:
        if count >= max_count:
            break
        yield value
        count += 1


def my_generator():
    for i in range(10):
        yield i

limited_generator = limit(my_generator(), 5)


for value in limited_generator:
    print(value)
