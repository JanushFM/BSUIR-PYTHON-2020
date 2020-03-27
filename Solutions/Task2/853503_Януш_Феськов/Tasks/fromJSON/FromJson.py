#This task wask almost fully copy-pasted https://github.com/eatonphil/pj but with:
#Some performance improvements
#Fixed error with null.

from Tasks.fromJSON.lexer import lex
from Tasks.fromJSON.parser import parse


def from_json(json_obj):
    tokens = lex(json_obj)
    return parse(tokens, is_root=True)[0]

