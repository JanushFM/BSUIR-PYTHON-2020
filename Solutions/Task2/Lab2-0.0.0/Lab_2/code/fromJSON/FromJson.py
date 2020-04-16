from Lab_2.code.fromJSON.lexer import lex
from Lab_2.code.fromJSON.parser import parse


def from_json(json_obj):
    tokens = lex(json_obj)
    return parse(tokens, is_root=True)[0]

