#!/usr/bin/python3
"""
A Flask application to display if a number is odd or even.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page with the number and whether it is odd or even."""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
