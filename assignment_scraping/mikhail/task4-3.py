import inspect

def inspect_function(func):
    """
    Takes another function as an argument (but not built-in) and prints the following data: 
    the name of the analyzed function, the names of all the arguments it takes, 
    and their types (positional, keyword, etc.).
    """
    func_name = func.__name__
    print(f"Function name: {func_name}")

    sig = inspect.signature(func)
    for name, param in sig.parameters.items():
        param_type = param.kind
        param_type_str = ''
        if param_type == param.POSITIONAL_ONLY:
            param_type_str = 'positional-only'
        elif param_type == param.POSITIONAL_OR_KEYWORD:
            param_type_str = 'positional or keyword'
        elif param_type == param.VAR_POSITIONAL:
            param_type_str = 'var positional (*args)'
        elif param_type == param.KEYWORD_ONLY:
            param_type_str = 'keyword-only'
        elif param_type == param.VAR_KEYWORD:
            param_type_str = 'var keyword (**kwargs)'
        
        print(f"Argument name: {name}, type: {param_type_str}")

# Example function to inspect
def example_function(pos_arg, *, kw_only_arg='default', **kwargs):
    pass

# Using the inspect_function
inspect_function(example_function)
