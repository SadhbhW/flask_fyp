import http.client, urllib.request, urllib.parse, urllib.error, base64
import pprint
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cd24a9a50c9f4f0cb057c77c28a6cae7',
}

params = urllib.parse.urlencode({
    # Request parameters
    'gtin': '7622400005190',
})

try:
    conn = http.client.HTTPSConnection('dev.tescolabs.com')
    conn.request("GET", "/product/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    item_data = response.read()
   # pprint.pprint(item_data)
   # print(type(item_data))
    conn.close()

    # convert byte array to json
    item_data_to_convert = (b'{\r\n  "products": [\r\n    {\r\n      "gtin": "07622400005190",\r\n      "t' b'pnb": "064226782",\r\n      "tpnc": "264875337",\r\n      "description": "Mi' b'lka Happy Cows Milk & White Chocolate Bar",\r\n      "brand": "MILKA",\r\n  'b'    "qtyContents": {\r\n        "quantity": 100.0,\r\n        "totalQuantity' b'": 100.0,\r\n        "quantityUom": "G",\r\n        "unitQty": "100G",\r\n' b'        "netContents": "100g \xe2\x84\xae",\r\n        "avgMeasure": "Avera'b'ge Measure (e)"\r\n      },\r\n      "productCharacteristics": {\r\n      'b'  "isFood": true,\r\n        "isDrink": false,\r\n        "healthScore": 18,' b'\r\n        "isHazardous": false,\r\n        "storageType": "Ambient",\r\n'b'        "isAnalgesic": false,\r\n        "containsLoperamide": false\r\n    'b'  },\r\n      "pkgDimensions": [\r\n        {\r\n          "no": 1,\r\n     ' b'     "height": 7.5,\r\n          "width": 16.2,\r\n          "depth": 1.' b'0,\r\n          "dimensionUom": "cm",\r\n          "weight": 104.0,\r\n   ' b'       "weightUom": "g",\r\n          "volume": 121.5,\r\n          "volumeU' b'om": "cc"\r\n        }\r\n      ]\r\n    }\r\n  ]\r\n}')

    converted_to_json = item_data_to_convert.decode('utf8').replace("'", '"')
    data = json.loads(converted_to_json)
    json_data = json.dumps(data, indent=4, sort_keys=True)
  # pprint.pprint(json_data)

    # write json data to json file
    json_to_file = open('itemdata.json', 'w')
    json.dump(json_data, json_to_file)
   # print(json_data)

    # read json file
    print("HI")

    # Opening JSON file
    f = open('itemdata.json', )

    # returns JSON object as
    # a dictionary
    print(">:(")
    data = json.load(f)
    json.loads(json_data.read())
    # error is here

    # Iterating through the json
    # list
    print("yay")
    for i in data['item_waste_details']:
        print(i)

    # Closing file
    f.close()

except Exception as e:
    print("error")
