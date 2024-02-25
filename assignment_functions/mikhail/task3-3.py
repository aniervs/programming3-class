import inspect

def inspect_function(func):
    """
    Takes another function as an argument (but not built-in) and prints the following data:
    - the name of the analyzed function,
    - the names of all the arguments it takes and their types (positional, keyword, etc.)
    """
    if not inspect.isfunction(func):
        print("Provided argument is not a function.")
        return

    function_name = func.__name__
    print(f"Function Name: {function_name}")

    signature = inspect.signature(func)
    for name, param in signature.parameters.items():
        if param.kind == param.POSITIONAL_ONLY:
            param_type = "Positional-only"
        elif param.kind == param.KEYWORD_ONLY:
            param_type = "Keyword-only"
        elif param.kind == param.VAR_POSITIONAL:
            param_type = "Arbitrary Positional (*args)"
        elif param.kind == param.VAR_KEYWORD:
            param_type = "Arbitrary Keyword (**kwargs)"
        else:
            param_type = "Positional or Keyword"
        
        print(f"Argument Name: {name}, Type: {param_type}")

# Example of how to use this function:
def example_function(a, b=1, *args, **kwargs):
    pass

inspect_function(example_function)
