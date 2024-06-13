#!/usr/bin/python3
"""
Launches a Flask web application
    Accessible on 0.0.0.0, port 5000
    URL routes: /:              displays "Hello HBNB!"
                /hbnb:          displays "HBNB"
                /c/<text>:      displays "C" followed by the provided text (underscores replaced with spaces)
                /python/<text>: displays "Python" followed by the provided text (default is "is cool")
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

@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays 'Python' followed by custom text
       The first route ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
