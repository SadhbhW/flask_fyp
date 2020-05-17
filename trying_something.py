import json
import pprint
with open(r"C:\Users\sadhb\PycharmProjects\flask_fyp\recyclesaurs\received_item_data.json", "r") as f:
    data = json.load(f)
    x = data['products']
    pprint.pprint(x)
