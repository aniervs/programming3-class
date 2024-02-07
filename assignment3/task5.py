


def limit(max_count, input_generator):
    """
        Limits the number of values yielded by an input generator.
        `max_count` specifies the maximum number of values to yield.
        `input_generator` is the generator to consume values from.
        This function is useful for controlling the amount of data processed.
        The main goal of yield is to use less memory
        For example, it creates a generator with values from 0 to 5
        But you can't print the generator directly
        You need to loop through it to ge the values, because they are not stored in memory
        They are stored in the generator
        """

    count = 0
    for value in input_generator:
        if count < max_count:
            yield value
            count += 1
        else:
            break

# Example usage:
generator = (i for i in range(10))
for value in limit(5, generator):
    print(value)


