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
