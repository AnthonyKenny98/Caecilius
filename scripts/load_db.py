"""Convert infile into json database."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-28 14:34:42
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 10:20:42

import sys
from os.path import dirname, realpath
import json

DATABASE = dirname(dirname(realpath(__file__))) + '/src/db/{}.txt'.format(
    sys.argv[2])

db = []

# Latin input
# with open(sys.argv[1], 'r') as infile:
#     for line in infile:
#         if line is not "\n":
#             (lat, eng) = line.strip("\n").split(" - ")
#             db.append({
#                 "phrase": lat,
#                 "translation": eng
#             })

# French Input
with open(sys.argv[1], 'r') as infile:
    for line in infile:
        if line is not "\n":
            (fre, eng) = line.strip("\n").split(" ::: ")
            db.append({
                "phrase": fre,
                "translation": eng.replace('lit.', 'literal:')
            })


with open(DATABASE, 'w') as f:
    f.write(json.dumps(db))
