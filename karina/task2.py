def check(s):
    lenn = 1
    palin = s[0]
    for i in range(len(s)):
        for j in range(len(s) - i):
            if s[i: i + j + 1] == s[i: i + j + 1][::-1] and len(s[i: i + j + 1]) > lenn:
                palin = s[i: i + j + 1]
                lenn = len(s[i: i + j + 1])
    return palin


print(check(input()))
