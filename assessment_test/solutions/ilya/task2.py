def find_longest_palindrome(left, right, input_str):
    while left >= 0 and right < len(input_str) and input_str[left] == input_str[right]:
        left -= 1
        right += 1
    return input_str[left + 1:right]


user_input = input()

longest_palindrome = user_input[0]

for i in range(len(user_input) - 1):
    odd_length_palindrome = find_longest_palindrome(i, i, user_input)
    even_length_palindrome = find_longest_palindrome(i, i + 1, user_input)

    if len(odd_length_palindrome) > len(longest_palindrome):
        longest_palindrome = odd_length_palindrome
    if len(even_length_palindrome) > len(longest_palindrome):
        longest_palindrome = even_length_palindrome

print(longest_palindrome)