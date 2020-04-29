"""Convert infile into json database."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-28 14:34:42
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 09:06:26

import sys
from os.path import dirname, realpath
import json

DATABASE = dirname(dirname(realpath(__file__))) + '/src/{}.txt'.format(
    sys.argv[2])

db = []
with open(sys.argv[1], 'r') as infile:
    for line in infile:
        if line is not "\n":
            (lat, eng) = line.strip("\n").split(" - ")
            db.append({
                "phrase": lat,
                "translation": eng
            })

with open(DATABASE, 'w') as f:
    f.write(json.dumps(db))
