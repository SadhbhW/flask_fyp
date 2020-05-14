from recyclesaurs import barcode_find
from flask import Flask, render_template, request
import json
import tempfile
import os
import base64

app = Flask(__name__)
DEBUG = True


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/image', methods=['POST', 'GET'])
def text():
    if request.is_json:
        image = request.json.get("imageData")
        if image:
            print("Image has been recognised")
            # Remove the header
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp:
                stripped = image.replace("data:image/png;base64,", "")
                decoded = base64.b64decode(stripped)
                temp.write(decoded)
                temp_path = temp.name
            parsed_barcodes = barcode_find.retrieve_barcode(temp_path)

            if not DEBUG:
                os.remove(temp_path)
            return json.dumps(parsed_barcodes), 200
        print("hi")


    return "OK"


@app.route('/results_page', methods=['GET', 'POST'])
def results_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
