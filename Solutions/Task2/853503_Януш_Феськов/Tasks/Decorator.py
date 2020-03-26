temp_list = []


def decorator_function(func):
    def wrapper(a, b):
        for s_list in temp_list:
            if a == s_list[0] and b == s_list[1]:
                return s_list[2]
            elif a == s_list[1] and b == s_list[0]:
                return s_list[2]

        temp_list.append([a, b, func(a, b)])
    return wrapper


@decorator_function
def summing(a, b):
    return a + b
