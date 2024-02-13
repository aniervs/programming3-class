def long_palindrome(s):   
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  
    longest = ""   
    for i in range(len(s)):
        palin_odd = expand_around_center(i, i)
        if len(palin_odd) > len(longest):
            longest = palin_odd
        palin_even = expand_around_center(i, i + 1)
        if len(palin_even) > len(longest):
            longest = palin_even
    return longest


print(long_palindrome("preferable"))