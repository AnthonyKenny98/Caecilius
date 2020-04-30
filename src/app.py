"""Main App."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-28 14:19:07
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 11:03:21

from flask import Flask, jsonify
from datetime import datetime
import json

import random

app = Flask(__name__)


@app.route('/<language>')
def phrase_of_the_dat(language):
    """Basic Respond."""
    try:
        with open('db/{}.txt'.format(language)) as f:
            db = json.loads(f.read())
    except FileNotFoundError:
        return jsonify({'error': 'language not available'})
    time = datetime.combine(datetime.today(), datetime.min.time()).timestamp()
    index = int(time % len(db))
    return jsonify(db[index])
