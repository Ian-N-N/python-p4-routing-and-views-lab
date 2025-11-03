from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)            # ✅ print only the text, not extra words
    return text            # ✅ return plain text (no HTML tags)

@app.route('/count/<int:n>')
def count(n):
    lines = [str(i) for i in range(n)]
    return Response('\n'.join(lines) + '\n', mimetype='text/plain')  # ✅ add final newline

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Division by zero is not allowed.', 400
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Modulo by zero is not allowed.', 400
        result = num1 % num2
    else:
        return 'Unsupported operation. Use +, -, *, div, or %.', 400

    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
