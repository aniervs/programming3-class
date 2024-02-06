def my_function(positional_arg, *args, default_arg, **kwargs):
    """
    This function demonstrates different types of arguments:

    Parameters:
    - positional_arg: A required positional argument.
    - default_arg: An optional positional argument with a default value of 10.
    - *args: Additional positional arguments passed as a tuple.
    - **kwargs: Additional keyword arguments passed as a dictionary.
    """
    print("Positional argument:", positional_arg)
    print("Default argument:", default_arg)
    print("Additional positional arguments (*args):", args)
    print("Additional keyword arguments (**kwargs):", kwargs)

my_function(1, 'a', 'b', 'c', default_arg=15, name='smth', n2='smth2')