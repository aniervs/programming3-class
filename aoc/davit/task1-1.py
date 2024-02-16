# get day1.txt
# PART 1
txt = None

with open('./txt/day1.txt', 'r') as file:

    
    txt = file.read()
    
    file.close()
        
def get_first_num(line:str):
    for letter in line:
        if letter.isdigit():
            return letter
        
def get_last_num(line:str):   
    for letter in line[::-1]:
        if letter.isdigit():
            return letter
     
res = 0
lines = txt.split('\n')

for line in lines:  
    first = get_first_num(line)
    last = get_last_num(line)
    if first == None or last == None:
        continue
    
    line_num = str(first) + str(last)

    res += int(line_num)
    
print(res)
    
#PART 2

values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
pairs = []

for line in lines:
    digits = []

    for i, c in enumerate(line):
        if line[i].isdigit():
            digits.append(line[i])
        else:
            for k in values.keys():
                if line[i:].startswith(k):
                    digits.append(values[k])
                    
    pairs.append(int(f"{digits[0]}{digits[-1]}"))
print(sum(pairs))