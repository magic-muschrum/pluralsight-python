'''
Created on 26.10.2018

@author: tpilz
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run()