def my_function(pos_arg, default_arg="default", *args, **kwargs):
    """
    A demonstration function showcasing different types of arguments.

    Parameters:
    pos_arg (required): A positional argument.
    default_arg (str, optional): A positional argument with a default value. Default is "default".
    *args: Arbitrary number of positional arguments.
    **kwargs: Arbitrary number of keyword arguments.

    Returns:
    dict: A dictionary containing all types of arguments received by the function.
    """
    result = {
        "positional_argument": pos_arg,
        "default_argument": default_arg,
        "arbitrary_args": args,
        "keyword_args": kwargs
    }
    return result

# Example of using this function:
my_function("positional", "custom_default", 1, 2, 3, key1="value1", key2="value2")
