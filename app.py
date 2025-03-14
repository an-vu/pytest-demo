#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
from art import get_art

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    art = get_art()
    return jsonify({"ascii_art": art})

if __name__ == '__main__':
    app.run(debug=True)

