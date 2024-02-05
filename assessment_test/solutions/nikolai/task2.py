def expand_from_center(left, right, str):
    while (left >= 0 and right < len(str) and str[left] == str[right]):
        left -= 1
        right += 1
    return str[left + 1: right]

string = input("Enter a string: ")

longest = string[0]

for i in range(len(string) - 1):
    oddLen = expand_from_center(i, i, string)
    evenLen = expand_from_center(i, i + 1, string)
    if len(oddLen) > len(longest):
        longest = oddLen
    if len(evenLen) > len(longest):
        longest = evenLen

print(longest)