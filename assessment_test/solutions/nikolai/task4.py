class DataBase:
    def __init__(self):
        self.DB = {}

    def SET(self, key, value):
        self.DB[key] = value

    def DELETE(self, key):
        if key in self.DB:
            del self.DB[key]
        else:
            print("NO SUCH USERNAME")

    def GET(self, key):
        return self.DB.get(key)

    def COUNT(self):
        return (len(self.DB))

    def GET_BY_AGE (self, age):
        keys = []
        for key, value in self.DB.items():
            if age == value:
                keys.append(key)
        return keys




db = DataBase()
while(True):
    query = input("Enter a query: ")
    query_arr = query.split(' ')
    if query_arr[0] == "SET":
        try:
            db.SET(query_arr[1], query_arr[2])
        except ValueError:
            print("Invalid query")

    elif query_arr[0] == "GET":
        try:
            print(db.GET(query_arr[1]))
        except ValueError:
            print("Invalid query")

    elif query_arr[0] == "DELETE":
        try:
            db.DELETE(query_arr[1])
        except ValueError:
            print("Invalid query")

    elif query_arr[0] == "COUNT":
        try:
            print(db.COUNT())
        except ValueError:
            print("Invalid query")

    elif query_arr[0] == "GET_BY_AGE":
        try:
            print(*db.GET_BY_AGE(query_arr[1]))
        except ValueError:
            print("Invalid query")
    else:
        print("Invalid query")