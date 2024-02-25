In this assignment, you'll be working with functions, generators, and decorators.

Instructions
Inside the solutions folder (programming3-class/assignment_functions/solutions/), create a folder with your name lowercase (for e.g., if your name is Anier, then your folder would be named anier).
Copy the given notebook inside the corresponding folder (in my case, I would have to copy it to programming3-class/assignment_functions/solutions/anier/) and solve the tasks.
Each of the tasks contains a line saying raise NotImplementedError. This is there in purpose. Once you've implemented a task, remove that line on that task.
Once you're done, make a PR with your commits.
Task 1
Write a function with documentation in a docstring (no need for a complicated documentation, just something very simple describing the function).

The function should contain all types of arguments (positional, positional with defaults, arbitrary args, keyword args, arbitrary keyword args).
def my_function():
    # your code here
    raise NotImplementedError
Task 2
A number is prime if it has 2 divisors exactly.

The first few primes are: 2, 3, 5, 7, 11, ...

Make a function that checks if a number is prime or not.

def is_prime(n: int) -> bool:
    """
    Checks if n is prime or not
    """
    # your code here
    raise NotImplementedError
Task 3
Implement the following function according to the docstring provided.

Read https://docs.python.org/3.11/library/inspect.html in order to see how to get each requested information.

import inspect

def inspect_function(func):
    """
    Takes another function as an argument (but not built-in) 
    and print the following data: 
    the name of the analyzed function, 
    the name of all the arguments it takes 
    and their types (positional, keyword, etc.)
    """
    # your code here
    raise NotImplementedError
Task 4
The following function isn't working properly. Fix it so that it prints the current datetime with a message.

from datetime import datetime
from time import sleep
 
# wrong function
def my_time_now(msg, *, dt=datetime.now()):
    print(msg, dt)
# simple tests :)
my_time_now('The time is now: ')
sleep(1)
my_time_now('The time is now: ')
sleep(1)
my_time_now('The time is now: ')
The time is now:  2024-02-06 01:06:05.034610
The time is now:  2024-02-06 01:06:05.034610
The time is now:  2024-02-06 01:06:05.034610
Task 5
Make a function that returns at most max_count values of a given generator.

def limit(input_generator, max_count):    
    """
    Generator that returns not more than max_count values of the input_generator.
    """
    # your code here
    raise NotImplementedError
Task 6
Write a generator for an infinite sequence of numbers from the Pascal's triangle. The sequence look like this: `1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 ... '

Test it with a generator from the previous task

# your code here
raise NotImplementedError
Task 7
Write a merge_sorter generator that merges sorted sequences of integers.

The generator takes an arbitrary number of arguments. The argument can be any iterable, including another generator. It is guaranteed that each argument is a sequence of integers, sorted in non-decreasing order.

def merge_sorter(*args):
    # your code here
    raise NotImplementedError
Task 8
Write the decorator proﬁler, which, when calling a function, will store in its attributes (not to be confused with arguments) the time of its execution (in seconds, it can be fractional) and the number of recursive calls that occurred during execution. Name the attributes last_time_taken and calls. It is forbidden to use global variables. The decorator must behave in a decent manner, that is, it must not overwrite the function's documentation.

For tests write Ackemann function.

def profiler():
    # your code here
    raise NotImplementedError

def ackermann(n: int, m: int) -> int:
    # your code here
    raise NotImplementedError