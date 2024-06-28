#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count=f''
    for i in range(number):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation,num2):
    if operation == '+':
        return f'<h1>The result of {num1} {operation} {num2}  = {num1 + num2}</h1>'
    elif operation == '-':
        return f'<h1>The result of {num1} {operation} {num2}  = {num1 - num2}</h1>'
    elif operation == '*':
        return f'<h1>The result of {num1} {operation} {num2}  = {num1 * num2}</h1>'
    elif operation == 'div':
        return f'<h1>The result of {num1} {operation} {num2}  = {num1 / num2}</h1>'
    elif operation == '%':
        return f'<h1>The result of {num1} {operation} {num2}  = {num1 % num2}</h1>'
    else:
        return '<h1>Syntax error!!</h1>'
    print(num1,operation,num2,'=',result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)