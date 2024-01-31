database = dict()

while True:
    line = input().split()
    command = line[0]
    if command == "SET":
        username, age = line[1], int(line[2])
        database[username] = age
        print(f"User {username} set to age = {age} successfully.")
    elif command == "GET":
        username = line[1]
        print(database.get(username, "No such user"))
    elif command == "DELETE":
        username = line[1]
        if username in database:
            database.pop(username)
            print("User deleted successfully.")
        else:
            print("No such user")
    elif command == "COUNT":
        print(len(database))
    elif command == "GET_BY_AGE":
        age = int(line[1])
        usernames = []
        for username, user_age in database.items():
            if user_age == age:
                usernames.append(username)
        print(usernames)
    elif command == "EXIT":
        break
    else:
        print("Invalid command")