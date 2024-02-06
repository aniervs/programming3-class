def pascals_triangle():
    """
    Generator for an infinite sequence of numbers from Pascal's triangle.
    """
    row = [1]
    yield 1

    while True:
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)  # End each row with 1

        for num in next_row:
            yield num

        row = next_row

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

limited_sequence = limit(pascals_triangle(), 100)

print(list(limited_sequence))
