class UserDatabase:
    def __init__(self):
        self.users = {}

    def set_user(self, username, age):
        self.users[username] = age

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise KeyError(f"User '{username}' not found")

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
        else:
            raise KeyError(f"User '{username}' not found")

    def count_users(self):
        return len(self.users)

    def get_by_age(self, age):
        return [username for username, user_age in self.users.items() if user_age == age]


def main():
    db = UserDatabase()
    while True:
        try:
            command = input("Enter command (SET, GET, DELETE, COUNT, GET_BY_AGE, or EXIT to stop): ")
            if command == "EXIT":
                break

            if command == "SET":
                username, age = input("Enter username and age: ").split()
                db.set_user(username, int(age))
                print(f"User '{username}' set with age {age}")

            elif command == "GET":
                username = input("Enter username: ")
                age = db.get_user(username)
                print(f"User '{username}' is {age} years old")

            elif command == "DELETE":
                username = input("Enter username to delete: ")
                db.delete_user(username)
                print(f"User '{username}' deleted")

            elif command == "COUNT":
                count = db.count_users()
                print(f"Total users: {count}")

            elif command == "GET_BY_AGE":
                age = int(input("Enter age: "))
                users = db.get_by_age(age)
                print(f"Users with age {age}: {', '.join(users)}")

            else:
                print("Invalid command")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
