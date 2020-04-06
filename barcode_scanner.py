from pyzbar import pyzbar
import cv2

def activate():
    video = cv2.VideoCapture(0)
    (camera_active, image) = video.read()

    while camera_active:
        cv2.imshow("image", image)

        barcodes = pyzbar.decode(image)

        # more than one detected barcode
        for barcode in barcodes:
            # bounding box location of barcode, drawn around barcode
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # convert barcode data from byte object to string
            barcode_byte = barcode.data.decode("utf-8")
            barcode_string = barcode.type

            # show barcode type and data to user
            print("The barcode {} {} was found".format(barcode_string, barcode_byte))
            # database = 'test_database.db'
            # db = sqlite3.connect(database)
            # cur = db.cursor()

            # cur.execute("""SELECT * FROM test_item where item_barcode = ?""", (barcode_byte,))
            # user_info = cur.fetchall()
            # pprint(user_info)

        key = cv2.waitKey(1)

        # stops repeated prints
        if len(barcodes) != 0:
            break

        # if video
        (camera_active, image) = video.read()

    video.release()
