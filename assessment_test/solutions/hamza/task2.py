

def palindrome(string):

    inverse_string = ""

    for i in range(len(string) - 1, -1, -1):
        inverse_string += string[i]

    longest_palindrome = ""

    # preferable elbareferp

    # if pr not in elbareferp
    # look for re
    # if re in elbareferp
    # look for ref in elbareferp


    #        "pr"
    #  if string[0:2] not in inverse_string:

    #         "re"
    #  if string[1:3] in inverse_string:
    #       longest_palindrome = "re

    #           "ref"
    #      if string[1:4] in inverse_string:
    #       longest_palindrome = "ref"

    # ongoing palindrome until "referab", because "referab" is not in "preferable"

    #        "referab"
    #    if string[1:8] in inverse_string:
    #          longest_palindrome is still "refer", because "referab" is not in "preferable"
    #    else:
    #          go to string[2:9]
    #




    from_index = 0
    to_index = 2

    while to_index < len(string) + 1:
        if string[from_index:to_index] in inverse_string:
            longest_palindrome = string[from_index:to_index]
            to_index += 1
        else:
            from_index += 1
            to_index += 1
    return longest_palindrome


print(palindrome("level"))


