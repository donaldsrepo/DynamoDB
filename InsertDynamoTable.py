import boto3
from boto3 import resource
from datetime import datetime

table = resource("dynamodb").Table("Customers")
response = table.put_item(
    Item={
        "last_name": "lastname-1",
        "state": "CA",
        "customer_id": "customer-1",
        "order_id": "order-1",
        "date": datetime.now().isoformat()
    }
)
print(f"response: {response}")
