import unittest
import random
from Lab_2.code.externalMergeSort.externalMergeSort import external_sort


def create_file(file_name):
    with open(file_name, "w") as f:
        f.writelines("{}\n".format(random.randint(-1000000, 1000000)) for _ in range(100000))


class TestSortMethods(unittest.TestCase):
    test_list = []

    def load_file(self, unsorted_file):
        with open(unsorted_file, "r") as f:
            for line in f:
                self.test_list.append(int(line))

    def compare(self, sorted_file_name):
        self.test_list.sort()
        with open(sorted_file_name, "r") as f:
            for el in self.test_list:
                if el != int(f.readline()):
                    return False
        return True

    def test_sort(self):
        unsorted_file_name = "numbers.txt"
        sorted_file_name = "sorted_file.txt"
        create_file(unsorted_file_name)
        external_sort(unsorted_file_name, sorted_file_name)
        self.load_file(unsorted_file_name)
        self.assertTrue(self.compare(sorted_file_name))

    def test_sort_exception(self):
        with self.assertRaises(Exception):
            external_sort("incorrect_name.txt", "sorted_file_name.txt")

if __name__ == '__main__':
    unittest.main()