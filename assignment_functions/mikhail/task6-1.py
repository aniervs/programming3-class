def pascals_triangle():
    """
    Generator for an infinite sequence of numbers from Pascal's Triangle.
    Yields each number in the triangle, row by row.
    """
    row = [1]
    while True:
        for element in row:
            yield element
        row = [x + y for x, y in zip([0] + row, row + [0])]

def limit(input_generator, max_count):
    """
    Generator that returns not more than max_count values from the input_generator.
    """
    count = 0
    for item in input_generator:
        if count < max_count:
            yield item
            count += 1
        else:
            break

# Example of how to use this function:
limited_gen = limit(pascals_triangle(), 20)
for num in limited_gen:
    print(num, end=' ')
