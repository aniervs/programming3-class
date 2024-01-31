class Database:
    def __init__(self):
        self.users = []

    def query(self, command):
        parts = command.split()
        type = parts[0].upper()

        if type == "SET":
            self.set_user(parts[1], int(parts[2]))
        elif type == "GET":
            return self.get_user(parts[1])
        elif type == "DELETE":
            self.delete_user(parts[1])
        elif type == "COUNT":
            return self.count_users()
        elif type == "GET_BY_AGE":
            return self.get_by_age(int(parts[1]))


    def set_user(self, username, age):
        for user in self.users:
            if user['username'] == username:
                user['age'] = age
                return
        self.users.append({'username': username, 'age': age})

    def get_user(self, username):
        for user in self.users:
            if user['username'] == username:
                return user['age']
        return -1

    def delete_user(self, username):
        self.users = [user for user in self.users if user['username'] != username]

    def count_users(self):
        return len(self.users)

    def get_by_age(self, age):
        return [user['username'] for user in self.users if user['age'] == age]


db = Database()

db.query("SET user1 45")
db.query("SET user2 47")
db.query("SET user3 45")
print(db.query("GET user2"))
print( db.get_by_age(45))
print(db.query("COUNT"))
print(db.query("DELETE user2"))
print(db.query("COUNT"))