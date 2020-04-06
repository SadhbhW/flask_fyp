from flask import render_template, Flask, request, redirect, url_for

from recyclesaurs import barcode_find

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')
    # return activate()

@app.route('/text', methods=['POST', 'GET'])
def text():
    print("hello")
    barcode_find.activate(request.data)
    return ("OK")


if __name__ == '__main__':
    app.run(debug=True)