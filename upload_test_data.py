import json
import boto3
import pprint
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.client(
    "dynamodb", aws_access_key_id=os.getenv("aws_access_key_id"), aws_secret_access_key=os.getenv("aws_secret_access_key")
)
table_name = os.getenv("table_name")

with open("data.json") as file:
    data = json.load(file)

print(data)
for item in data:
    response = dynamodb.put_item(TableName=table_name, Item=item)
    print(item.get("clubId"))
