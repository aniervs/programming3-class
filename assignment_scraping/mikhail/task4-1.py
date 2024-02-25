def demo_function(pos_arg, pos_default_arg='default', *args, **kwargs):
    """
    Demonstrates the use of different types of function arguments in Python.

    Args:
    - pos_arg: A mandatory positional argument.
    - pos_default_arg: A positional argument with a default value.
    - *args: Arbitrary number of positional arguments.
    - **kwargs: Arbitrary number of keyword arguments.

    Returns:
    A dictionary with all arguments organized by type.
    """
    return {
        "positional_argument": pos_arg,
        "positional_default_argument": pos_default_arg,
        "arbitrary_positional_arguments": args,
        "keyword_arguments": kwargs
    }

# Example usage
result = demo_function(
    'mandatory positional', 
    'optional positional', 
    'extra positional 1', 
    'extra positional 2', 
    keyword1='value1', 
    keyword2='value2'
)

print(result)
