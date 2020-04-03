import subprocess

from flask import render_template, Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')
    # return activate()

@app.route('/text', methods=['POST', 'GET'])
def text():
    print("hello")
    # if request.method == "POST":
        # subprocess.call(['python', 'barcode_scanner.py'])
       # return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
