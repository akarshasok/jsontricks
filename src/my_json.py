import json
from pprint import pprint

with open("data.json") as json_file:
    data = json.load(json_file)


pprint(data[0].keys())
#dict_keys(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

d = [i.get('InvoiceNo') for i in data ]
print(d)
#[536370, 536372, 536389, 562106]

# updating one dict value in json based on condition
update_dict = {
    "InvoiceNo": 1,
    "StockCode": 1,
    "Description": "Updated dict",
    "Quantity": 1,
    "InvoiceDate": "9/9/9999 9:99",
    "UnitPrice": 1,
    "CustomerID": 1,
    "Country": "Nowhere"
}
for i in data:
    if i.get("InvoiceNo") == 536370 :
        i.update(update_dict)
pprint(data)

#writing it as a new json file

with open("newdata.json", "w") as json_file:
    json.dump(data,json_file)