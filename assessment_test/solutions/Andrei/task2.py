# simple method, complexity O(n^3)

def longestPal_simple(s):
    maxlen = 0
    ans = ''
    for i in range(len(s)):
        for j in range(i,len(s)):
            cur = s[i:j+1]
            # print(cur)
            if cur == cur[::-1] and j-i+1 > maxlen:
                ans = cur
                maxlen = j-i+1

    return ans

print(longestPal_simple("preferable"))
print(longestPal_simple('abacaba'))




#smart method, complexity O(n^2)

def longestPal_smart(s):
    longest = []
    n = len(s)
    for i in range(n):
        longest.append([])
        for j in range(n):
            if i == j:
                longest[i].append(1)
            elif i > j:
                longest[i].append(0)
            else:
                longest[i].append(-1)

    def findlength(left, right):
        if longest[left][right] == -1:
            if s[left] == s[right]:
                longest[left][right] = findlength(left+1, right-1) + 2
            else:
                longest[left][right] = max(findlength(left+1, right), findlength(left, right-1))
        return longest[left][right]
    
    length = findlength(0, n-1)
    ans = [''] * length

    def build_pal(left, right, ans_left, ans_right):
        while left <= right:
            if left == right and longest[left][right] == 1:
                ans[ans_left] = s[left]
                ans_left += 1
                left += 1
            else:
                if s[left] == s[right]:
                    ans[ans_left] = s[left]
                    ans_left += 1
                    left += 1
                    ans[ans_right] = s[right]
                    ans_right -= 1
                    right -= 1
                else:
                    if longest[left + 1][right] >= longest[left][right - 1]:
                        left += 1
                    else:
                        right -= 1

    build_pal(0, n-1, 0, length-1)
    return ''.join(ans)

print(longestPal_smart('preferable'))
print(longestPal_smart('abacaba'))
print(longestPal_smart('abcde'))