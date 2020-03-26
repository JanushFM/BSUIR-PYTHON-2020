import unittest
import json
from Tasks.toJSON.toJSON_v1 import encoder1
from Tasks.toJSON.toJSON_v2 import encoder2
from Tasks.fromJSON.FromJson import from_json

obj = {
    "in_dic1": {"a": 1, "b": 2, "c": 3,
                "in_in_dic1": {"a": 4, "b": 5, "c": "6",
                               "in_in_in_dic1": {"a": 7, "b": 8, "c": "9"}}},
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

SIMPLE_DICT = '{"pets": null, "name": "John"}'
COMPLEX_DICT = '{"in_dic2": {"a": 1, "b": 2, "c": 3}, "name": "John", "age": 30, "married": true, "divorced": false, ' \
               '"children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": ' \
               '"Ford ' \
               'Edge", "mpg": 24.1}]} '
exception_str = '{name: Janush, age: 19}'


class TestJsonMethods(unittest.TestCase):
    def test_str(self):
        self.assertEqual(encoder1(obj), json.dumps(obj))
        self.assertEqual(encoder2(obj), json.dumps(obj))

    def test_for_from_json_simple(self):
        self.assertEqual(from_json(SIMPLE_DICT), json.loads(SIMPLE_DICT))

    def test_for_from_json_complex(self):
        self.assertEqual(from_json(COMPLEX_DICT), json.loads(COMPLEX_DICT))

    def test_incorrect_s(self):
        with self.assertRaises(Exception):
            from_json(exception_str)


if __name__ == '__main__':
    unittest.main()
