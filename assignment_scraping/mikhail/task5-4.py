import requests
from bs4 import BeautifulSoup
import functools
import unittest

class ComputerScientist:
    def __init__(self, name, gender, birthdate, major_achievements, alma_mater):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.major_achievements = major_achievements
        self.alma_mater = alma_mater

    def __repr__(self):
        return (f"ComputerScientist(name={self.name}, gender={self.gender}, birthdate={self.birthdate}, "
                f"major_achievements={self.major_achievements}, alma_mater={self.alma_mater}, "
                f"wikipedia_link={getattr(self, 'wikipedia_link', None)})")

@functools.lru_cache(maxsize=None)
def fetch_scientist(scientist_name):
    base_url = "https://en.wikipedia.org/wiki/"
    search_url = base_url + scientist_name.replace(" ", "_")

    try:
        response = requests.get(search_url)
        response.raise_for_status()  

        if "may refer to:" in response.text or "Wikipedia does not have an article with this exact name." in response.text:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        scientist = ComputerScientist(name=scientist_name, gender=None, birthdate=None, major_achievements=None, alma_mater=None)

        setattr(scientist, 'wikipedia_link', search_url)

        return scientist

    except requests.RequestException:
        return None

class TestComputerScientist(unittest.TestCase):
    def test_fetch_scientist(self):
        scientist = fetch_scientist("Alan Turing")
        self.assertIsNotNone(scientist)
        self.assertEqual(scientist.name, "Alan Turing")
        self.assertTrue(hasattr(scientist, 'wikipedia_link'))

    def test_fetch_non_existent_scientist(self):
        scientist = fetch_scientist("Non Existent Scientist")
        self.assertIsNone(scientist)

if __name__ == '__main__':
    unittest.main()
