

def pascals_triangle():
    """
        Generates an infinite sequence of numbers from Pascal's triangle.
        Pascal's triangle is a triangular array of the binomial coefficients.
        This generator yields each number in the triangle row by row.
        In the pascals_triangle function, yield is used to give out each number in the sequence one by one,
        row by row of Pascal's triangle.
        It makes Pascal's triangle one number at a time.
        And because it uses yield, it can keep doing this indefinitely,
        generating the next part of the triangle only when asked for,
        This is perfect for pascal's triangle because eventhough you generate an infinite triangle,
        it will not cause memory issues
        """

    row = [1]
    while True:
        # Yield every element in the current row
        for element in row:
            yield element
        # Prepare the next row
        row = [x + y for x, y in zip([0]+row, row+[0])]

def limit(max_count, input_generator):

    count = 0
    for value in input_generator:
        if count < max_count:
            yield value
            count += 1
        else:
            break

for value in limit(20, pascals_triangle()):
    print(value, end=' ')
