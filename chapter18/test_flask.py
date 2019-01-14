#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 00:32:47 2019

@author: mitsuo
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

app.run(port='8080')
