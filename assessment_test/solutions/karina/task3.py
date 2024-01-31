def check(lst):
    dups = dict()
    ls = []
    for el in lst:
        if dups.keys().__contains__(el):
            dups[el] = dups[el] + 1
        else:
            dups[el] = 1
    for el in dups:
        if dups[el] > 1:
            ls.append(el)
    return ls


lst = map(int, input().split())
print(check(lst))
