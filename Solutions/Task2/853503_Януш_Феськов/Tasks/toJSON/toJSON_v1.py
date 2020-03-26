def encoder1(dictionary):
    string = str(dictionary)

    string = string.replace("'", '"')
    string = string.replace("False", "false")
    string = string.replace("True", "true")
    string = string.replace("None", "null")
    string = string.replace("(", "[")
    string = string.replace(")", "]")

    return string

if __name__ == '__main__':
    BOOL = ["TruE", True, False, "false", 1, 0]
    import json
    print(json.dumps(BOOL))