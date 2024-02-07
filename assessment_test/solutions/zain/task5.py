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

input_gen = (x for x in range(10)) 
max_count = 5

limited_gen = limit(input_gen, max_count)

for value in limited_gen:
    print(value)
