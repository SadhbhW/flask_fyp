import http.client, urllib.request, urllib.parse, urllib.error, base64
import pprint
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cd24a9a50c9f4f0cb057c77c28a6cae7',
}

params = urllib.parse.urlencode({
    # Request parameters
    'gtin': '5391517591453',
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
    item_data_to_convert = item_data
    converted_to_json = item_data_to_convert.decode('utf8').replace("'", '"')
    data = json.loads(converted_to_json)
    json_data = json.dumps(data, indent=4, sort_keys=True)
  # pprint.pprint(json_data)

    # write json data to json file
    json_to_file = open('received_item_data.json2', 'w')
    json.dump(json_data, json_to_file)
    print(json_data)


except Exception as e:
    print("error")
