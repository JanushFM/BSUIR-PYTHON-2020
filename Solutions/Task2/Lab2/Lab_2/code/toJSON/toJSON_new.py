import json


def dumps(obj):
    if isinstance(obj, str):
        return '"' + obj + '"'
    if isinstance(obj, bool):
        return str(obj).lower()
    if isinstance(obj, (int, float)):
        return str(obj)
    if obj is None:
        return "null"
    if isinstance(obj, (list, tuple)):
        return "[" + ", ".join([dumps(el) for el in obj]) + "]"

    if isinstance(obj, dict):
        keys = [str(v) if isinstance(v, (int, float)) else v for v in obj.keys()]
        for k in keys:
            if not isinstance(k, (int, float, str)):
                raise TypeError("keys must be str, int, float, bool or None, not {}".format(type(k).__name__))

        return "{" + ', '.join(
            ["{}: {}".format(dumps(k), dumps(v)) for k, v in zip(keys, obj.values())]) + "}"


if __name__ == '__main__':
    test1 = {
        23: True,
        "2": "14",
        "children": ("Ann", "Billy"),
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "pets": None
    }

    test2 = {
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

    original = json.dumps(test2)
    mine = dumps(test2)
    print(original == mine)
