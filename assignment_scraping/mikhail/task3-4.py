from bs4 import BeautifulSoup
import requests
import unittest
from unittest.mock import patch

def get_pages_depth(url: str, depth: int):

    visited = set()  

    def _fetch_links(current_url, current_depth):
        if current_depth > depth or current_url in visited:
            return
        visited.add(current_url)

        try:
            response = requests.get(current_url)
            response.raise_for_status()
            yield response.text
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                link_url = link.get('href')
                link_url = requests.compat.urljoin(current_url, link_url)  
                if link_url not in visited:
                    yield from _fetch_links(link_url, current_depth + 1)
        except requests.RequestException:
            pass  

    yield from _fetch_links(url, 0)

class TestGetPagesDepth(unittest.TestCase):

    def setUp(self):
        self.mock_html_page_1 = '<html><body><a href="https://httpbin.org/links/10/1">Link page</a></body></html>'
        self.mock_html_page_link = '<html><body><a href="https://httpbin.org">Home</a></body></html>'

        self.url_mapping = {
            'https://httpbin.org/links/10/0': self.mock_html_page_1,
            'https://httpbin.org/links/10/1': self.mock_html_page_link,
        }

    def mock_requests_get(self, url):
        class MockResponse:
            def __init__(self, text, status_code):
                self.text = text
                self.status_code = status_code

            def raise_for_status(self):
                if self.status_code != 200:
                    raise requests.HTTPError()

        if url in self.url_mapping:
            return MockResponse(self.url_mapping[url], 200)
        return MockResponse('', 404)

    @patch('requests.get')
    def test_function_returns_html_content(self, mock_get):
        mock_get.side_effect = self.mock_requests_get

        pages = get_pages_depth('https://httpbin.org/links/10/0', depth=1)
        content = list(pages)
        self.assertIn(self.mock_html_page_1, content)
        self.assertIn(self.mock_html_page_link, content)

    @patch('requests.get')
    def test_no_duplicate_pages_returned(self, mock_get):
        mock_get.side_effect = self.mock_requests_get

        pages = get_pages_depth('https://httpbin.org/links/10/0', depth=2)
        content = set(pages) 
        self.assertEqual(len(content), 2) 

    @patch('requests.get')
    def test_respects_specified_depth(self, mock_get):
        mock_get.side_effect = self.mock_requests_get

        pages = get_pages_depth('https://httpbin.org/links/10/0', depth=0)
        content = list(pages)
        self.assertEqual(len(content), 1)
        self.assertIn(self.mock_html_page_1, content)

    @patch('requests.get')
    def test_handles_exceptions_gracefully(self, mock_get):
        mock_get.return_value.raise_for_status.side_effect = requests.HTTPError()

        pages = get_pages_depth('https://httpbin.org/status/404', depth=1)
        with self.assertRaises(StopIteration):
            next(pages)

if __name__ == '__main__':
    unittest.main()