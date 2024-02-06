import unittest

# this function only returns each duplicate once
def find_duplicates(a):
    sorted_a = sorted(a)
    n = len(a)
    result = []

    for i in range(1, n-1):
        if sorted_a[i-1] == sorted_a[i] and sorted_a[i] != sorted_a[i + 1]:
            result.append(sorted_a[i])

    # edge case: biggest number is duplicated
    if n >= 2 and sorted_a[n-1] == sorted_a[n-2]:
        result.append(sorted_a[n-1])

    return result

class TestDuplicates(unittest.TestCase):
    def test_duplicates(self):
        a = [6, 4, 78, 3, 4, 7, 6, 78, 78, 1]
        self.assertEqual(find_duplicates(a), [4, 6, 78])

    def test_no_duplicates(self):
        a = [6, 4, 5, 9, 2]
        self.assertEqual(find_duplicates(a), [])

    def test_empty(self):
        self.assertEqual(find_duplicates([]), [])

    def test_one_number(self):
        self.assertEqual(find_duplicates([4]), [])

    def test_one_kind_of_number(self):
        self.assertEqual(find_duplicates([6, 6, 6, 6, 6, 6]), [6])

if __name__ == '__main__':
    unittest.main()
