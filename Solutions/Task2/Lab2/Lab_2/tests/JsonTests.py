import unittest
import json
from ..code.toJSON.toJSON_new import dumps

from ..code.fromJSON.FromJson import from_json

COMPLEX_DICT = '{"in_dic2": {"a": 1, "b": 2, "c": 3}, "name": "John", "age": 30, "married": true, "divorced": false, ' \
               '"children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": ' \
               '"Ford ' \
               'Edge", "mpg": 24.1}]} '
exception_str1 = '{name: Janush, age: 19}'
exception_str2 = '{"num: "52"}'
exception_str3 = '}"num": "52"'
exception_str4 = '{25:"num"}'
exception_str5 = '{"name" "Janush"}'
exception_str6 = '{"name" : "Janush" "age": 25}'

exception_str7 = '{"children": ["Ann" "Billy"]}'


class TestJsonMethods(unittest.TestCase):

    def test_for_from_json_complex(self):
        self.assertEqual(from_json(COMPLEX_DICT), json.loads(COMPLEX_DICT))

    def test_to_JSON(self):
        temp = from_json(COMPLEX_DICT)
        self.assertEqual(dumps(temp), json.dumps(temp))

    def test_incorrect_to_JSON(self):
        with self.assertRaises(Exception):
            dumps({(1, 2): "name"})

    def test_incorrect_1(self):
        with self.assertRaises(Exception):
            from_json(exception_str1)

    def test_incorrect_2(self):
        with self.assertRaises(Exception):
            from_json(exception_str2)

    def test_incorrect_3(self):
        with self.assertRaises(Exception):
            from_json(exception_str3)

    def test_incorrect_4(self):
        with self.assertRaises(Exception):
            from_json(exception_str4)

    def test_incorrect_5(self):
        with self.assertRaises(Exception):
            from_json(exception_str5)

    def test_incorrect_6(self):
        with self.assertRaises(Exception):
            from_json(exception_str6)

    def test_incorrect_7(self):
        with self.assertRaises(Exception):
            from_json(exception_str7)


if __name__ == '__main__':
    unittest.main()
