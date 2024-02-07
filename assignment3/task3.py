
import inspect
def function3(x,*numbers, y=True,**person):

    pass

def inspect_function(function):
    """
        Prints the name and parameters of a function.
        It shows each parameter's name and whether it is positional, keyword-only, or accepts variable numbers of arguments.
        This is useful for understanding how to call the function and what kinds of arguments it accepts.
        """

    print(function.__name__)

    sig = inspect.signature(function)


    for name, param in sig.parameters.items():

        parameter_type = 'POSITIONAL OR KEYWORD'

        if param.kind == param.POSITIONAL_ONLY:
            parameter_type = 'POSITIONAL ONLY'

        elif param.kind == param.KEYWORD_ONLY:
            parameter_type = 'KEYWORD ONLY'

        elif param.kind == param.VAR_POSITIONAL:
            parameter_type = 'VAR POSITIONAL (*args)'

        elif param.kind == param.VAR_KEYWORD:
            parameter_type = 'VAR KEYWORD (**kwargs)'

        print(f" Parameter name: {name}, Type: {parameter_type}")

inspect_function(function3)

