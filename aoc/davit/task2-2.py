import re

def sum_powers():
    power_sum = 0
    with open("txt/games.txt", "r") as file:
        sets_pattern = "(?<=:)(.*)"
        r_pattern = "(\\d+)(?=\\sred)"
        g_pattern = "(\\d+)(?=\\sgreen)"
        b_pattern = "(\\d+)(?=\\sblue)"

        for line in file:
            r_max = g_max = b_max = 0
            sets = re.search(sets_pattern, line).group(0)
            sets = re.split(";", sets)
            
            for s in sets:
                r_val = re.search(r_pattern, s)
                if r_val:
                    r_val = int(r_val.group(0))
                    if r_val > r_max: r_max = r_val

                g_val = re.search(g_pattern, s)
                if g_val:
                    g_val = int(g_val.group(0))
                    if g_val > g_max: g_max = g_val

                b_val = re.search(b_pattern, s)
                if b_val:
                    b_val = int(b_val.group(0))
                    if b_val > b_max: b_max = b_val
                    
            power = r_max * g_max * b_max
            power_sum += power

    print(power_sum)
    
sum_powers()
