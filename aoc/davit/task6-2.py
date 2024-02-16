with open('./txt/day6.txt', 'r') as f:
    c = f.read().splitlines()

t_vals = [int(i) for i in c[0].split(': ')[1].split(' ') if i]
d_vals = [int(i) for i in c[1].split(': ')[1].split(' ') if i]

td_pairs = list(zip(t_vals, d_vals))

print(td_pairs)

def calc_excd(td):
    excd_cnt = 0
    
    for delta in range(1, td[0]):
        comp_d = (td[0] - delta) * delta
        if comp_d > td[1]:
            excd_cnt += 1
    return excd_cnt

cum_res = 1

for p in td_pairs:
    cum_res *= calc_excd(p)

print(cum_res)

conc_t = ''.join(c[0].split(': ')[1].split(' '))
conc_d = ''.join(c[1].split(': ')[1].split(' '))

final_td = (int(conc_t), int(conc_d))

print(calc_excd(final_td))
