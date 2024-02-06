import inspect

def inspect_function(func):
    """
    Takes another function as an argument (but not built-in)
    and print the following data:
    the name of the analyzed function,
    the name of all the arguments it takes
    and their types (positional, keyword, etc.)
    """
    # Get the function name
    print("Function Name:", func.__name__)

    signature = inspect.signature(func)

    for param_name, param in signature.parameters.items():
        print("Parameter:", param_name)
        print("Parameter Type:", param.kind)

# Example usage:
def example_function(a, b, *args, c=1, d=2, **kwargs):
    pass

inspect_function(example_function)
