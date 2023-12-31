import boto3
from boto3.dynamodb.conditions import Key, Attr

region = "us-west-1"
dynamodb = boto3.resource('dynamodb', region_name=region)
table = dynamodb.Table("Customers")

response = table.get_item(Key={'last_name': 'lastname-1', 'state': 'CA'})
print(f"item returned: {response['Item']}")
