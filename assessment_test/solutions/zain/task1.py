
def my_function(positional_arg, default_arg="1", *args, keyword_arg="2", **kwargs):
    """
    Function consiting of arguments 
    
    positional_arg is a positional argument.
    default_arg is a positional argument with a default value.
    *args is an rbitrary positional arguments.
    keyword_arg is a keyword argument with a default value.
    *kwargs is an Arbitrary keyword arguments.
    
    """
    result = f"positional_arg: {positional_arg}, default_arg: {default_arg}, args: {args}, keyword_arg: {keyword_arg}, kwargs: {kwargs}"
    return result

result = my_function("positional", keyword_arg="keyword_arg", additional_arg1="1", additional_arg2="2")
print(result)

def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    while left < right and top < bottom:
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiral_order(test_matrix))



