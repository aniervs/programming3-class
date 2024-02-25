def calculate_excess_count(td):
    excess_cnt = 0

    for delta in range(1, td[0]):
        comp_d = (td[0] - delta) * delta
        if comp_d > td[1]:
            excess_cnt += 1

    return excess_cnt

with open('task6.txt', 'r') as f:
    lines = f.read().splitlines()

t_vals = [int(i) for i in lines[0].split(': ')[1].split() if i]
d_vals = [int(i) for i in lines[1].split(': ')[1].split() if i]

td_pairs = list(zip(t_vals, d_vals))

cumulative_result = 1

for p in td_pairs:
    cumulative_result *= calculate_excess_count(p)

print(cumulative_result)