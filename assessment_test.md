# Assesment test

## Instructions
1. Clone this repository.
2. Create a folder with your name lowercase (for e.g: my name is Anier, hence the folder's name is `anier`).
3. For each the remaining tasks, create a file whose name is `task<NUMBER>.py` that will contain your code for that task. For example, for the second task, you should create a file `task2.py`. These files should be inside the folder with your name.
4. Solve the tasks you can. Follow the format (once again, a folder whose name is your name lowercase, that will contain the code for the tasks you solved. The file for the task `<NUMBER>` should be named `task<NUMBER>.py`).
5. By the end of the exam, make a Pull Request with your changes.

### Note

Any code MUST BE TESTED. Add some simple tests to your code, to make sure it works (no need for very comprehensive tests, just one or two per task is enough).

## Task 1

Write a function that takes a 2D array (ie: a matrix) and returns all the elements of the matrix in spiral order.

## Task 2

Write a function that takes a set of numbers and it will return all the possible subsets. For example, for the set `{1, 2, 3}`, the output should be (not necessarily in the same order):
```
[{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
```


## Task 3

Write a function that takes a list of integers and finds any duplicates, returning them in a new list. If there are no duplicates, it should return an empty list. Make it as efficient as you can.

## Task 4

- Make a code that will simulate a database of users.
- It will store the age of each user. Do it with simple Python, key-value storage. NO NEED TO USE A REAL DATABASE.
- It should support the following operations:
    - `SET <username> <age>`: This operation will create a user the given name and age. If a user with that name already exists, then it will replace their age with the new one.
    - `GET <username>`: This will return the age of the user with the given name. If no user with that name exists, the program should raise an exception (if you don't know what an exception is, then just return None or -1).
    - `DELETE <username>`: This will delete the user with the given name from the database. Similar behaviour to above's for the case when no user with the given name exists.
    - `COUNT`: This will return the number of users in the databse.
    - `GET_BY_AGE <age>`: This will return all the users with the given age. Return an empty list if there's no user with that age.


## Task 5
- Create a script that scans through a specified directory and its subdirectories, to find files that match certain criteria (e.g., file extension, file size, creation date, name).
- The script should output the list of files that meet the given conditions.
- Consider using libraries like `os` or `pathlib`. Alternatively, if you know how to, you can call shell scripts from python.
