# FirstCommand="SET"
# FC=FirstCommand.islower()

# SecondCommand="Get by age"
# SC=SecondCommand.islower()

def set_age(name, age):
    ages[name] = age
    return "UPDATED"

def get_age(name):
    if name in ages:
        return ages[name]
    else:
        return "ERROR!"
    
def delete_person(name):
    if name in ages:
        del ages[name]
        return "DELETED"
    else:
        return "ERROR!"
def count():
    return len(ages)
def by_age(age):
    names = [name for name, person_age in ages.items() if person_age == age]
    return names
def parse_command(command):
    if command.startswith("SET"):
        return set_age(command.split()[1], int(command.split()[2]))
    elif command.startswith("GET_BY_AGE"):
        return by_age(int(command.split()[1]))
    elif command.startswith("DELETE"):
        return delete_person(command.split()[1])
    elif command.startswith("COUNT"):
        return count()
    elif command.startswith("GET"):
        return get_age(command.split()[1])
    else:
        return "COMMAND DOES NOT EXIST."
ages = {}
while True:
    print(parse_command(input("Enter your command: ")))


