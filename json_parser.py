import json

import logging_aux


@logging_aux.logger_wraps()
def replace_characters(json_string):
    forbidden_chars = [{'old': '\n', 'new': '\u2424'}, {'old': '\/', 'new': '/'}, {'old': '\'', 'new': '%27'}]
    for char in forbidden_chars:
        json_string = str.replace(json_string, char['old'], char['new'])
    return json_string


@logging_aux.logger_wraps()
def decode_json(json_str):
    json_str = replace_characters(json_str)
    obj_arr = json.loads(json_str)
    return obj_arr


@logging_aux.logger_wraps()
def encode_json(res_obj):
    json_str = json.dumps(res_obj)
    return json_str
