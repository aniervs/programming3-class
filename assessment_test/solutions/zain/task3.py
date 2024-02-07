import inspect

def inspect_function(func):
    """
    Takes another function as an argument (but not built-in) 
    and prints information about its name and parameters.
    """
    signature = inspect.signature(func)

    print(f"Function Name: {func.__name__}")

    for param_name, param in signature.parameters.items():
        
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else "No type specified"
        
        if param.kind == inspect.Parameter.POSITIONAL_ONLY:
            kind = "Positional Only"
        elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            kind = "Positional or Keyword"
        elif param.kind == inspect.Parameter.VAR_POSITIONAL:
            kind = "Variable Positional (*args)"
        elif param.kind == inspect.Parameter.KEYWORD_ONLY:
            kind = "Keyword Only"
        elif param.kind == inspect.Parameter.VAR_KEYWORD:
            kind = "Variable Keyword (**kwargs)"
    print(f"Parameter: {param_name}, Type: {param_type}, Kind: {kind}")
