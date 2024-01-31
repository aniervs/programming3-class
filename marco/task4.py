import unittest

users = {}

def run_command(command):
    words = command.split()
    if len(words) == 0:
        raise Exception("Empty line")

    if words[0] == "SET":
        if len(words) != 3:
            raise Exception(f"Incorrect number of arguments for SET. Expected 2, received {len(words)}.")
        user_name = words[1]
        user_age = int(words[2])
        users[user_name] = user_age

    elif words[0] == "GET":
        if len(words) != 2:
            raise Exception(f"Incorrect number of arguments for GET. Expected 1, received {len(words)}.")
        user_name = words[1]
        if user_name not in users:
            raise Exception(f"User with the name {user_name} doesn't exists.")
        return users[user_name]

    elif words[0] == "DELETE":
        if len(words) != 2:
            raise Exception(f"Incorrect number of arguments for DELETE. Expected 1, received {len(words)}.")
        user_name = words[1]
        if user_name not in users:
            raise Exception(f"User with the name {user_name} doesn't exists.")
        del users[user_name]

    elif words[0] == "COUNT":
        if len(words) != 1:
            raise Exception(f"Incorrect number of arguments for COUNT. Expected 0, received {len(words)}.")
        return len(users)

    elif words[0] == "GET_BY_AGE":
        if len(words) != 2:
            raise Exception(f"Incorrect number of arguments for GET_BY_AGE. Expected 1, received {len(words)}.")
        query_age = int(words[1])
        result = []
        for user_name, user_age in users.items():
            if user_age == query_age:
                result.append(user_name)
        return result

    else:
        raise Exception(f"Unknown command '{words[0]}'")

class TestDatabase(unittest.TestCase):
    def tearDown(self):
        global users
        users = {}

    def test_set_get(self):
        run_command("SET marco 21")
        self.assertEqual(run_command("GET marco"), 21)

    def test_delete(self):
        with self.assertRaises(Exception):
            run_command("GET marco")
        run_command("SET marco 21")
        self.assertEqual(run_command("GET marco"), 21)
        run_command("DELETE marco")
        with self.assertRaises(Exception):
            run_command("GET marco")

    def test_count(self):
        self.assertEqual(run_command("COUNT"), 0)
        run_command("SET marco 21")
        self.assertEqual(run_command("COUNT"), 1)
        run_command("SET anier 5")
        self.assertEqual(run_command("COUNT"), 2)
        run_command("SET marco 22")
        self.assertEqual(run_command("COUNT"), 2)

    def test_get_by_age(self):
        self.assertEqual(run_command("GET_BY_AGE 21"), [])
        run_command("SET marco 21")
        self.assertEqual(run_command("GET_BY_AGE 21"), ["marco"])
        run_command("SET anier 22")
        self.assertEqual(run_command("GET_BY_AGE 22"), ["anier"])
        run_command("SET marco 22")
        self.assertEqual(run_command("GET_BY_AGE 22"), ["marco", "anier"])

if __name__ == '__main__':
    unittest.main()
