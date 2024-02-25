import requests
from bs4 import BeautifulSoup
import random
import unittest
from unittest.mock import patch

class ComputerScientist:
    def __init__(self, name, gender, birthdate, major_achievements, alma_mater):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.major_achievements = major_achievements
        self.alma_mater = alma_mater

    def __repr__(self):
        return f"ComputerScientist(name={self.name}, gender={self.gender}, birthdate={self.birthdate}, " \
               f"major_achievements={self.major_achievements}, alma_mater={self.alma_mater})"

class TestComputerScientist(unittest.TestCase):
    def test_computer_scientist(self):
        cs = ComputerScientist(
            name="Alan Turing",
            gender="Male",
            birthdate="1912-06-23",
            major_achievements="Turing machine, Turing test",
            alma_mater="King's College, Cambridge"
        )
        self.assertEqual(cs.name, "Alan Turing")
        self.assertEqual(cs.gender, "Male")
        self.assertEqual(cs.birthdate, "1912-06-23")
        self.assertEqual(cs.major_achievements, "Turing machine, Turing test")
        self.assertEqual(cs.alma_mater, "King's College, Cambridge")

def scrape_wikipedia_for_scientists(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    scientist_links = soup.select('div.mw-category-group ul li a[href]')
    unique_scientist_links = list(set(a['href'] for a in scientist_links if a['href'].startswith('/wiki/')))

    random_scientist_links = random.sample(unique_scientist_links, min(100, len(unique_scientist_links)))

    computer_scientists = []

    return computer_scientists

if __name__ == '__main__':
    
    unittest.main(exit=False)

    scientists_list_url = 'https://en.wikipedia.org/wiki/List_of_computer_scientists'
    computer_scientists = scrape_wikipedia_for_scientists(scientists_list_url)
    print(computer_scientists)
