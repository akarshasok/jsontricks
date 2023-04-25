# jsonschema is an implementation of the JSON Schema specification for Python.

import pytest
import json
from src.validatejson import validate_json_schema

class Test_JSONValidation:

    def test_validate_json_schema_Should_return_False_when_invalid_json_schema(self):
        # Arrange
        #InvoiceNo is string instead of int
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

        # Act
        is_valid_json_schema, message = validate_json_schema(
            InvoiceNo_is_a_string,  my_schema=transaction_schema)
        # Assert
        assert is_valid_json_schema == False
        assert message == 'Given JSON data is not valid '

    def test_validate_json_schema_Should_return_True_when_valid_json_schema(self):
        # Arrange
        valid_json_schema = {
            "InvoiceNo": 536370,
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France",
            "CustomerID": 12583,
        }

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

        # Act
        is_valid_json_schema, message = validate_json_schema(
            valid_json_schema,  my_schema=transaction_schema)
        # Assert
        assert is_valid_json_schema == True
        assert message == "Given JSON is valid."


    # this test only runs if the pytest.ini has the *_test set
    def run_validate_json_schema_Should_return_True_when_valid_json_schema_test(self):
        # Arrange
        valid_json_schema = {
            "InvoiceNo": 536370,
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France",
            "CustomerID": 12583,
        }

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

        # Act
        is_valid_json_schema, message = validate_json_schema(
            valid_json_schema,  my_schema=transaction_schema)
        # Assert
        assert is_valid_json_schema == True
        assert message == "Given JSON is valid."
