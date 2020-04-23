import unittest
import random
from ..code.externalMergeSort.externalMergeSort import external_sort


def create_file(file_name):
    with open(file_name, "w") as f:
        f.writelines("{}\n".format(random.randint(-1000000, 1000000)) for _ in range(100000))


class TestSortMethods(unittest.TestCase):

    def compare(self, sorted_file_name):
        with open(sorted_file_name) as fp:
            prev_int = int(fp.readline())
            for line in fp:
                next_int = int(line)
                self.assertTrue(next_int >= prev_int)
                prev_int = next_int

    def test_sort(self):
        unsorted_file_name = "numbers.txt"
        sorted_file_name = "sorted_file.txt"
        create_file(unsorted_file_name)
        external_sort(unsorted_file_name, sorted_file_name)
        self.compare(sorted_file_name)

    def test_sort_exception(self):
        with self.assertRaises(Exception):
            external_sort("incorrect_name.txt", "sorted_file_name.txt")

if __name__ == '__main__':
    unittest.main()