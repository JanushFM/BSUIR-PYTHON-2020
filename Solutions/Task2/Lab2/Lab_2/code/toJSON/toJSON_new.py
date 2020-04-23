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
