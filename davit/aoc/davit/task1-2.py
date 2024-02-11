txt = None

with open('./txt/day1.txt', 'r') as file:
    
    txt = file.read()
    
    file.close()

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

res = 0
lines = txt.split('\n')

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