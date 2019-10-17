# -*- coding: UTF-8 -*-

import json
import sys
import os

def parse_dicts(frequency_path):
    with open(frequency_path, 'r') as load_f:
        lines = load_f.readlines()
    print("总词量为", len(lines))
    result = []
    for d in lines:
        word=d.split(' ')[0]
        if len(word)>0:
            result.append(word)
    return result
