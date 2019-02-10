from flask import Flask, render_template, make_response
app = Flask(__name__)

temp = '13'

@app.route('/weather')
def hello():
    vxml = render_template('weather.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1partA')
def lab1():
    vxml = render_template('lab1partA.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1partB')
def lab1():
    vxml = render_template('menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response
