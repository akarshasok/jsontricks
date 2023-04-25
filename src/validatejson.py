import json
# jsonschema is an implementation of the JSON Schema specification for Python.
import jsonschema
from jsonschema import validate
from pprint import pprint

transaction_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
            "InvoiceNo": {
                "type": "integer"
            },
        "StockCode": {
                "type": "integer"
                },
        "Description": {
                "type": "string"
                },
        "Quantity": {
                "type": "integer",
                },
        "InvoiceDate": {
                "type": "string"
                },
        "UnitPrice": {
                "type": "number"
                },
        "CustomerID": {
                "type": "integer"
                },
        "Country": {
                "type": "string"
                }
    },
    "required": [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice"

    ]
}

#creating a json validation function

def validate_json_schema(json_data, my_schema):

    schema = my_schema
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is not valid "
        return False, err
    error_message = "Given JSON is valid."
    return True, error_message


if __name__ == "__main__":
    with open("data.json") as json_file:
        data = json.load(json_file)


        res1 = validate_json_schema(data[0],transaction_schema)
        print(res1)
        print("################")

        InvoiceNo_is_a_string = {
            "InvoiceNo": "536370",
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France",
            "CustomerID": 12583,
        }
        res2 = validate_json_schema(InvoiceNo_is_a_string,transaction_schema)
        print(res2)
        print("################")


        invalid_json_string = '{"InvoiceNo": 536370 "StockCode": 22492, "Description":  "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45",   "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'
        res3=validate_json_schema(invalid_json_string,transaction_schema)
        print(res3)
