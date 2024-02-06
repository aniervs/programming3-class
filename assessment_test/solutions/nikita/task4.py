users = {}

while True:
    prompt = input().split()
    operation = prompt[0]
    if operation == 'SET':
        name, age = prompt[1], int(prompt[2])
        users[name] = age
        print('User set')
    elif operation == 'GET':
        name = prompt[1]
        print(users.get(name, 'No user found'))
    elif operation == 'DELETE':
        name = prompt[1]
        if name in users:
            users.pop(name)
            print('User deleted')
        else:
            print("No user found")
    elif operation == 'COUNT':
        print(len(users))
    elif operation == 'GET_BY_AGE':
        age = int(prompt[1])
        names = []
        for user in users:
            if users[user] == age:
                print(user)
    else:
        print('Invalid operation')