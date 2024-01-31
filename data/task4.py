class Database:
    def __init__(self):
        self.users = {}
        self.ages_count = {}
        self.user_length = 0

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
        if username in self.users:
            self.delete_user(username)  
        if self.ages_count.get(age, None) == None:
            self.ages_count[age] = set()
        self.ages_count[age].add(username)
        self.users[username] = age
        self.user_length += 1

    def get_user(self, username):
        if self.users.get(username, -1) != -1:
            return self.users[username]
        return None

    def delete_user(self, username):
        if self.users.get(username, -1) != -1:
            age = self.users[username]
            if self.ages_count.get(age, []):   
                self.ages_count[age].remove(username)
            self.user_length -= 1
            del self.users[username]
            return True

    def count_users(self):
        return self.user_length

    def get_by_age(self, age):
        return self.ages_count[age]


db = Database()

db.query("SET user1 45")
db.query("SET user2 47")
db.query("SET user3 45")
print(db.query("GET user2"))
print(db.query("GET_BY_AGE 45"))
print(db.query("COUNT"))
print(db.query("DELETE user2"))
print(db.query("DELETE user1"))
print(db.query("COUNT"))
print(db.query("GET_BY_AGE 45"))
