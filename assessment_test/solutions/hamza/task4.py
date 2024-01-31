


class Employees:
    def __init__(self, employees):
        self.employees = employees

    def set(self, name, age):
        self.employees[name] = age


    def get(self, name):
        if name in self.employees:
            return self.employees[name]
        else:
            return None

    def delete(self, name):
        if name in self.employees:
            del self.employees[name]
            print(f"Employee '{name}' deleted")
        else:
            print(f"Employee '{name}' not found.")

    def count(self):
        return len(self.employees)

    def get_by_age(self, age):
        list1 = []
        for key , value in self.employees.items():
            if value == age:
                list1.append(key)
        return list1


# Example usage
employees = Employees({"Jack": 23, "Max": 21, "Jenny": 18})
employees.set("John", 22)
employees.get("Max")
employees.delete("Jack")
print(employees.count())
print(employees.get_by_age(21))




# Example of creating an instance of the class and using it

