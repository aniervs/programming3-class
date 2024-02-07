def is_palindrome(s):
    return s == s[::-1]

def find_palindrome(s:str)->str:    
    n = len(s)
    for size in range(n, 0, -1):
        answer = None 
        for i in range(n - size + 1):
            if is_palindrome(s[i:i+size]):
                answer = s[i:i+size]
                break 
        if answer is not None:
            return answer
        
assert find_palindrome("level") == "level"
assert find_palindrome("abcde") == "a"
assert find_palindrome("preferable") == "refer"
