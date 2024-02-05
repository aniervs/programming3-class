import unittest

# I am using a palindromic tree to solve this problem in O(n)
def longest_palindrome(s):
    position = [0, 0]
    length = [-1, 0]
    suffix = [0, 0]
    edges = [{}, {}]
    cur = 0
    for i in range(len(s)):
        while i - 1 - length[cur] < 0 or s[i - 1 - length[cur]] != s[i]:
            cur = suffix[cur]

        # check if this edge already exists
        if s[i] in edges[cur]:
            cur = edges[cur][s[i]]
            continue

        # create a new vertex
        length.append(length[cur] + 2)
        edges[cur][s[i]] = len(edges)
        edges.append({})
        position.append(i - length[cur] - 1)

        # find longest suffix of vertex
        new_suffix = suffix[cur]
        while s[i - 1 - length[new_suffix]] != s[i]:
            new_suffix = suffix[new_suffix]
        suffix.append(edges[new_suffix][s[i]])

        cur = edges[cur][s[i]]
        if suffix[cur] == cur:
            suffix[cur] = 1
            
    max_length = max(length)
    for i in range(len(length)):
        if length[i] == max_length:
            return s[position[i]:position[i]+length[i]]
    return ""

class TestPalindrome(unittest.TestCase):
    def test_palindromes(self):
        palindromes = [
            "level",
            "tacocat",
            "rotator",
            "civic",
        ]
        for palindrome in palindromes:
            self.assertEqual(longest_palindrome(palindrome), palindrome)

    def test_not_palindrome(self):
        words = [
            "snake",
            "conda",
            "python",
        ]
        for word in words:
            self.assertEqual(len(longest_palindrome(word)), 1)

    def test_partial(self):
        self.assertEqual(longest_palindrome("preferable"), "refer")

if __name__ == '__main__':
    unittest.main()
