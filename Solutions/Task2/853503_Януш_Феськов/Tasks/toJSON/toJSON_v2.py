import json


def list_encoder(list_tuple):
    json_str = ""
    for el in list_tuple:
        if isinstance(el, dict):
            json_str += encoder2(el)
        elif isinstance(el, (list, tuple)):
            json_str += list_encoder(el)
        elif isinstance(el, str):
            json_str += '"' + el + '"'
        elif isinstance(el, bool):
            json_str += str(el).lower()
        elif el is None:
            json_str += "null"
        else:
            json_str += str(el)
        json_str += ', '
    json_str = json_str[:-2]
    return "[" + json_str + "]"


def encoder2(dictionary):
    json_str = ""
    for key in dictionary:
        json_str += '"' + key + '": '
        if isinstance(dictionary[key], dict):
            json_str += encoder2(dictionary[key])
        elif isinstance(dictionary[key], (list, tuple)):
            json_str += list_encoder(dictionary[key])
        elif isinstance(dictionary[key], str):
            json_str += '"' + dictionary[key] + '"'
        elif isinstance(dictionary[key], bool):
            json_str += str(dictionary[key]).lower()
        elif dictionary[key] is None:
            json_str += "null"
        else:
            json_str += str(dictionary[key])
        json_str += ', '
    json_str = json_str[:-2]  # removed 2 last elements in str
    json_str = "{" + json_str + "}"
    return json_str


test1 = {
    "children": ("Ann", "Billy"),
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "pets": None,

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


