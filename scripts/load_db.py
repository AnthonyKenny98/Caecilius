"""Convert infile into json database."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-28 14:34:42
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 09:44:36

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
# https://en.wikipedia.org/wiki/Glossary_of_French_expressions_in_English
with open(sys.argv[1], 'r') as infile:
    lines = list(infile)
    for i in range(int(len(lines) / 2)):
        (french, eng) = lines[i * 2], lines[i * 2 + 1]
        # (french, eng) = line.strip("\n").split(" - ")
        db.append({
            "phrase": french.strip("\n"),
            "translation": eng.strip("\n")
        })


with open(DATABASE, 'w') as f:
    f.write(json.dumps(db))
