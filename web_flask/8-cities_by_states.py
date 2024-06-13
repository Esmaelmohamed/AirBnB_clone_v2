#!/usr/bin/python3
"""
Launches a Flask web application
    Accessible on 0.0.0.0, port 5000
    URL routes: /:                       displays "Hello HBNB!"
                /hbnb:                   displays "HBNB"
                /c/<text>:               displays "C" followed by the provided text (underscores replaced with spaces)
                /python/<text>:          displays "Python" followed by the provided text (default is "is cool")
                /number/<n>:             displays "<n> is a number" only if <n> is an integer
                /number_template/<n>:    displays an HTML page only if <n> is an integer
                /number_odd_or_even/<n>: displays an HTML page indicating if <n> is odd or even
                /states_list:            displays an HTML page with state information from storage
                /cities_by_states:       displays an HTML page with state and city relationships
"""
from models import storage
from flask import Flask, render_template

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

@app.route('/number/<int:n>')
def text_if_int(n):
    """Displays '<n> is a number' only if an integer is provided"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def html_if_int(n):
    """Displays an HTML page only if an integer is provided
       Inserts the provided integer into the HTML template
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def html_odd_or_even(n):
    """Displays an HTML page indicating if the provided integer is odd or even
       Inserts the provided integer and its odd/even status into the HTML template
    """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)

@app.teardown_appcontext
def tear_down(self):
    """Closes the current SQLAlchemy session after each request"""
    storage.close()

@app.route('/states_list')
def html_fetch_states():
    """Displays an HTML page with a list of states
       Fetches and sorts states to insert into an HTML template within a UL tag
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html', state_objs=state_objs)

@app.route('/cities_by_states')
def html_fetch_cities_by_states():
    """Displays an HTML page with a list of states and their cities
       Fetches and sorts states and their respective cities to insert into an HTML template within UL and LI tags
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('8-cities_by_states.html', state_objs=state_objs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
