from bs4 import BeautifulSoup
import requests
import unittest

def get_neighbor_pages(url: str):

    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            link_url = link.get('href')
            try:
                link_response = requests.get(link_url)
                link_response.raise_for_status()
                yield link_response.text
            except requests.RequestException:
                yield f"Error: Could not fetch the page at {link_url}"
    except requests.RequestException as e:
        yield f"Error: {e}"

class TestGetNeighborPages(unittest.TestCase):
    def test_get_neighbor_pages(self):
        url = "https://www.imdb.com/name/nm0331516/bio/"
        pages = list(get_neighbor_pages(url))
        self.assertTrue(len(pages) > 0)
        self.assertTrue(any("html" in page or "Error:" in page for page in pages))

if __name__ == '__main__':
    unittest.main()
