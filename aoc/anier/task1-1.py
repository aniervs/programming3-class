# read all the lines
# for each line, find the leftmost and rightmost digits
# create the number with those digits
# add up all the numbers

file = open("day1.input")

lines = file.readlines()

result = 0

for line in lines:
    line = line.strip()
    for c in line:
        if c.isnumeric(): # 0-9
            first_digit = int(c) 
            break 
    for c in line[::-1]:
        if c.isnumeric(): # 0-9
            last_digit = int(c)
            break 
    number = first_digit * 10 + last_digit
    result += number
    
print(result)
            

file.close()
