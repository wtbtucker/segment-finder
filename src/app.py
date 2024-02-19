#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <h1>Segment Finder</h1>
    <form action="/echo_user_input" method="POST">
        <label for="user_input">Zip Code</label><br>
        <input name="user_input">
        <input type="submit" value="Submit!">
    </form>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text