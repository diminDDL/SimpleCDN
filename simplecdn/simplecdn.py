#  Copyright (c) 2022 diminDDL
from flask import Flask


app = Flask(__name__)

visiotr = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/visitor')
def visitor():
    visiotr = visiotr + 1
    visitor_num = visiotr
    return "Visitor: %s" % (visitor_num)

@app.route('/visitor/reset')
def reset_visitor():
    visiotr = 0
    visitor_num = visiotr
    return "Visitor is reset to %s" % (visitor_num)