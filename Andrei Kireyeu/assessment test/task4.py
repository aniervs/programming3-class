users = {}

def set_user(name, age):
    users[name] = age

def get_user(name):
    return users[name]
    

def delete_user(name):
    users.pop(name)

def count():
    return len(users)

def get_by_age(age):
    result = []
    for i in users:
        if users[i] == age:
            result.append(i)
    return result

q = input('Provide a number of queries: ')
print('Queries:')
for i in range(int(q)):
    query = input().split()
    if query[0] == 'SET':
        set_user(query[1], int(query[2]))
    elif query[0] == 'GET':
        print(get_user(query[1]))
    elif query[0] == 'DELETE':
        delete_user(query[1])
    elif query[0] == 'COUNT':
        print(count())
    elif query[0] == 'GET_BY_AGE':
        print(*get_by_age(int(query[1])))
    else:
        print("Such command doesn't exist.")

