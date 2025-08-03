## Create a simple Flask application demonstrating various routing and rendering techniques

from flask import Flask, render_template, request, redirect, url_for

## Initialize the Flask application
## __name__ helps Flask determine the location of the application for templates, static files, etc.
app = Flask(__name__)

## Predefined list of technologies to be displayed in templates
techLst = ["Python", ".Net", "Machine Learning", "SQL", "Deep Learning", "Generative AI", "FullStack development", "Flask"]

## Route: Default root URL
## Returns a simple HTML response when a user accesses the homepage ('/')
@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

## Route: '/adminReroute'
## Demonstrates a simple route returning a direct HTML response
@app.route('/adminReroute')
def adminReroute():
    return "<h2>Hello, World! from adminReroute</h2>"

## Route: '/welcome/<name>'
## Demonstrates dynamic URL parameter capturing.
## Displays a personalized welcome message using the provided 'name' parameter.
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Welcome to the Flask Tutorials, {name}!</h1>"

## Route: '/admin'
## Demonstrates redirection using url_for().
## Redirects the request to another endpoint 'adminReroute'.
@app.route('/admin')
def admin():
    return redirect(url_for("adminReroute"))

## Route: '/adminName'
## Demonstrates redirection with dynamic URL parameters.
## Redirects to 'welcome' route and passes 'Suraj Admin' as the 'name' parameter.
@app.route('/adminName')
def adminName():
    return redirect(url_for("welcome", name="Suraj Admin"))

## Route: '/index'
## Renders an HTML template named 'index.html' from the 'templates' directory.
@app.route('/index')
def index():
    return render_template('index.html')

## Route: '/hello/<name>/<sname>'
## Demonstrates passing multiple dynamic URL parameters to an HTML template.
## Renders 'hello.html' and passes 'name' and 'sname' to the template.
@app.route('/hello/<name>/<sname>')
def hello(name, sname):
    return render_template('hello.html', name=name, sname=sname)

## Route: '/even/<int:range>'
## Demonstrates passing an integer dynamic parameter to a template.
## Renders 'even.html' and passes the range to display even numbers dynamically.
@app.route('/even/<int:range>')
def even(range):
    return render_template('even.html', seriesRange=range)

## Route: '/tech'
## Demonstrates passing a list from Python to an HTML template.
## Renders 'tech.html' and passes 'techLst' to be iterated in the template.
@app.route('/tech')
def tech():
    return render_template('tech.html', techLst=techLst)

## Entry point for running the Flask application.
## debug=True enables the interactive debugger and auto-reload during development.
if __name__ == '__main__':
    app.run(debug=True)
