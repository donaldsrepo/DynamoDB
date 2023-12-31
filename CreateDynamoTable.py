import boto3

DynamoClient = boto3.client("dynamodb")

new_table = DynamoClient.create_table(
    TableName="Customers",
    KeySchema=[
        {
            "AttributeName": "last_name",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "state",
            "KeyType": "RANGE"
        }
    ],
    AttributeDefinitions=[
        {
            "AttributeName": "last_name",
            "AttributeType": "S"
        },
        {
            "AttributeName": "state",
            "AttributeType": "S"
        },
    ],
    ProvisionedThroughput={
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1
    }
)