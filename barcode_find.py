from pyzbar import pyzbar
import cv2
# requests

def activate(data):
    while():
        barcodes = pyzbar.decode(data)

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


        # stops repeated prints
        if len(barcodes) != 0:
            break

# construct request
# to json
# back to front end through ajax
# useful info to user
# pwa, css for responsive design
# celinium (python automatic testing)
