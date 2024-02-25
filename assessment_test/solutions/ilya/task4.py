users = {}

while True:
    prompt = input().split()

    if not prompt:
        print("Invalid input. Please enter a valid command.")
        continue

    operation = prompt[0]
    if operation == 'SET' and len(prompt) == 3:
        name, age = prompt[1], int(prompt[2])
        users[name] = age
        print('User set')
    elif operation == 'GET' and len(prompt) == 2:
        name = prompt[1]
        print(users.get(name, 'No user found'))
    elif operation == 'DELETE' and len(prompt) == 2:
        name = prompt[1]
        if name in users:
            users.pop(name)
            print('User deleted')
        else:
            print("No user found")
    elif operation == 'COUNT' and len(prompt) == 1:
        print(len(users))
    elif operation == 'GET_BY_AGE' and len(prompt) == 2:
        age = int(prompt[1])
        names = [user for user, user_age in users.items() if user_age == age]

        if not names:
            print(f"No names found at age {age}")
        else:
            for name in names:
                print(name)
    else:
        print('Invalid operation or incorrect number of arguments')
