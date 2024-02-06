# read all the lines
# for each line, find the leftmost and rightmost digits
# create the number with those digits
# add up all the numbers

file = open("day1.input")

lines = file.readlines()

result = 0

candidates = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [str(i) for i in list(range(1, 10))]

def get_digit(candidate):
    if candidate.isnumeric():
        return int(candidate)  
    return candidates.index(candidate) + 1


for line in lines:
    line = line.strip()
    first_digit = None 
    last_digit = None 
    
    min_pos = int(1e9)
    max_pos = int(-1)
    
    for c in candidates:
        p1 = line.find(c)
        if p1 != -1:
            if min_pos > p1:
                min_pos = p1 
                first_digit = get_digit(c)
        
        p2 = line[::-1].find(c[::-1])
        if p2 != -1:
            p2 = len(line) - p2 - 1
            if max_pos < p2:
                max_pos = p2 
                last_digit = get_digit(c)
    
    number = first_digit * 10 + last_digit
    result += number 
    
print(result)
    



file.close()
