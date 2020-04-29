"""Main App."""
# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-04-28 14:19:07
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-04-30 08:57:23

from flask import Flask, jsonify
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/latin')
def index():
    """Basic Respond."""
    with open('db.txt') as f:
        db = json.loads(f.read())
    time = datetime.combine(datetime.today(), datetime.min.time()).timestamp()
    index = int(time % len(db))
    return jsonify(db[index])
