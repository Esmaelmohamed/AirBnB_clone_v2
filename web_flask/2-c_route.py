#!/usr/bin/python3
"""
Starts a Flask web application
    Runs on 0.0.0.0, port 5000
    URL routes: /:         displays "Hello HBNB!"
                /hbnb:     displays "HBNB"
                /c/<text>: displays "C" followed by the given text (underscores replaced with spaces)
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """Returns a greeting message"""
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """Returns the message 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>')
def c_text(text):
    """Displays 'C' followed by custom text"""
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
