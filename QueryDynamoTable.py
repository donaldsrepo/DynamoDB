import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name=region)
table = dynamodb.Table("Customers")
# or
table = resource("dynamodb").Table("Customers")

response = table.get_item(Key={'subscription_id': mysubid})
# or
response = table.query(
    IndexName='order_number-index',
    KeyConditionExpression=Key('order_number').eq(myordernumber))