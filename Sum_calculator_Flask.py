from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return 'Enter two numbers in the URL to add them. Example: /add/2/3'

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    result = num1 + num2
    return f"The sum of {num1} and {num2} is {result}"

if __name__ == "__main__":
    app.run()
