from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)

temp = '13'

@app.route('/weather')
def hello():
    vxml = render_template('weather.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/menu')
def menu():
    vxml = render_template('menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response    

@app.route('/lab2')
def lab2():
    vxml = render_template('lab2.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/delayed')
def delayed():
    vxml = render_template('delayed.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/booking')
def booking():
    vxml = render_template('booking.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab3')
def lab3():
    vxml = render_template('lab3.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)
