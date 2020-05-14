import pprint

from pyzbar import pyzbar
import cv2
import http.client, urllib.request, urllib.parse, urllib.error
import json

def retrieve_barcode(data):
    data = cv2.imread(data)

    barcodes = pyzbar.decode(data)
    parsed_barcodes = []
    # more than one detected barcode
    for barcode in barcodes:
        # bounding box location of barcode, drawn around barcode
        (x, y, w, h) = barcode.rect
        cv2.rectangle(data, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # convert barcode data from byte object to string
        barcode_byte = barcode.data.decode("utf-8")
        barcode_string = barcode.type

        # show barcode type and data to user
        print("The barcode {} {} was found in the image".format(barcode_string, barcode_byte))
        parsed_barcodes.append([barcode_string, barcode_byte])


        # api code
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': 'cd24a9a50c9f4f0cb057c77c28a6cae7',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'gtin': barcode_byte,
        })
        try:
            print("Requesting information from API...")
            conn = http.client.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", "/product/?%s" % params, "{description}", headers)
            response = conn.getresponse()
            item_data = response.read()
            conn.close()

            # convert byte array to json
            item_data_to_convert = item_data
            converted_to_json = item_data_to_convert.decode('utf8').replace("'", '"')
            data = json.loads(converted_to_json)
            json_data = json.dumps(data, indent=4, sort_keys=True)

            # write json data to json file
            json_to_file = open('received_item_data.json', 'w')
            json.dump(json_data, json_to_file)
            # print(json_data)

        except Exception as e:
            print("error")

    return parsed_barcodes
