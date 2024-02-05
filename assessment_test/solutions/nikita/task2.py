def longPal(word):
    n = len(word)
    maxLength = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            fl = 1

            for k in range(0, ((j - i) // 2) + 1):
                if (word[i + k] != word[j - k]):
                    fl = 0

            if (fl != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1


    return word[start:start+maxLength]
print(longPal("level"))
print(longPal("abcde"))
print(longPal("preferable"))