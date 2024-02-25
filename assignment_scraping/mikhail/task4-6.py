def pascals_triangle():
    """
    Generator for an infinite sequence of numbers from Pascal's triangle.
    """
    row = [1]
    while True:
        for num in row:
            yield num
        row = [x + y for x, y in zip([0]+row, row+[0])]

def limit(input_generator, max_count):
    count = 0
    for value in input_generator:
        if count < max_count:
            yield value
            count += 1
        else:
            break

limited_pascals = limit(pascals_triangle(), 20)

for value in limited_pascals:
    print(value, end=' ')
