from bs4 import BeautifulSoup
import requests
import unittest

def get_all_links(url: str):
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            yield link.get('href')
    except requests.RequestException as e:
        yield f"Error: {e}"

class TestGetAllLinks(unittest.TestCase):
    def test_get_all_links_valid_url(self):
        """Test that the function can fetch links from a valid URL."""
        url = "https://en.wikipedia.org/wiki/Ryan_Gosling"  
        links = list(get_all_links(url)) 
        self.assertTrue(len(links) > 0) 

    def test_get_all_links_invalid_url(self):
        """Test that the function yields an error message for an invalid URL."""
        url = "https://invalidurl.com"
        links = list(get_all_links(url))
        self.assertTrue("Error:" in links[0])  

if __name__ == '__main__':
    unittest.main()
