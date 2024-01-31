def set_age(name, age):
    ages.update([(name, age)])
    return "UPDATE successful"


def get_age(name):
    if ages.keys().__contains__(name):
        return ages[name]
    else:
        return Exception("Key doesn't exist")


def delete_person(name):
    if ages.keys().__contains__(name):
        ages.pop(name)
        return "DELETE successful"
    else:
        return Exception("Key doesn't exist")


def count():
    return len(ages)


def get_by_age(age):
    names = []
    for item in ages:
        if ages[item] == age:
            names.append(item)
    return names


def parse_command(command):
    if command.startswith("SET"):
        return set_age(command.split()[1], int(command.split()[2]))
    elif command.startswith("GET_BY_AGE"):
        return get_by_age(int(command.split()[1]))
    elif command.startswith("DELETE"):
        return delete_person(command.split()[1])
    elif command.startswith("COUNT"):
        return count()
    elif command.startswith("GET"):
        return get_age(command.split()[1])
    else:
        return Exception("No such command")


ages = dict()
while True:
    print(parse_command(input()))



