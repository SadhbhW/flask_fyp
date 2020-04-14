import http.client, urllib.request, urllib.parse, urllib.error, base64
import pprint

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cd24a9a50c9f4f0cb057c77c28a6cae7',
}

params = urllib.parse.urlencode({
    # Request parameters
    'gtin': '5000201499776',
})

try:
    conn = http.client.HTTPSConnection('dev.tescolabs.com')
    conn.request("GET", "/product/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    item_data = response.read()
    pprint.pprint(item_data)
    conn.close()
except Exception as e:
    print("error")
