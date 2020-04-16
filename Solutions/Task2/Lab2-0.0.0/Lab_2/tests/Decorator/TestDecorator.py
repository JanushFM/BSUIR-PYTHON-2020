from Lab_2.code.Decorator.Decorator import Cached
import unittest


@Cached
def summing(*args):
    result = 0
    for el in args:
        result += el
    return result


class TestDecorator(unittest.TestCase):
    def test(self):
        self.assertEqual(summing(1, 2, 3, 4), 10)
        self.assertEqual(summing(1, 2, 3, 4), 10)

if __name__ == '__main__':
    unittest.main()
