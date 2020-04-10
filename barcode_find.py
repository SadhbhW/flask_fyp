from pyzbar import pyzbar
import cv2
import http.client, urllib.request, urllib.parse, urllib.error, base64


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
        print("The barcode {} {} was found".format(barcode_string, barcode_byte))
        parsed_barcodes.append([barcode_string, barcode_byte])


        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': 'cd24a9a50c9f4f0cb057c77c28a6cae7',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'gtin': "barcode_byte",
        })
        print(barcode_byte)
        try:
            print("cunt")
            conn = http.client.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", "/product/?%s" % params, "{description}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("error")

    return parsed_barcodes

