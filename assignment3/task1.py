def my_function(a, b=42, *args, c, d=100, **kwargs):
    """
    A demonstration function that includes every type of argument.

    Parameters:
    - a: Positional argument: the one the user chooses
    - b: An optional positional argument with a default value.
    - *args: Arbitrary positional arguments: several arguments like numbers sent at once
    - c: A mandatory keyword argument.
    - d: An optional keyword argument with a default value.
    - **kwargs: Arbitrary keyword arguments: several objects like person="john" sent at once
    """
    print(f"Mandatory positional argument a: {a}")
    print(f"Optional positional argument with default b: {b}")
    print(f"Arbitrary positional arguments (*args): {args}")
    print(f"Mandatory keyword argument c: {c}")
    print(f"Optional keyword argument with default d: {d}")
    print(f"Arbitrary keyword arguments (**kwargs): {kwargs}")


# Example usage
my_function(1, 2, 3, 4, 5, c=6, d=7, e=8, f=9, g=10)
