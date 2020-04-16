
class Cached:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        f_result = self.func(*args)
        self.cache[args] = f_result
        return f_result
