import json
import boto3
import os

def lambda_handler(event, context):
    userId = event["user"]
   
    for item in userData:
        if userData[item] == "":
            userData[item] = " "
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table( os.environ["USERS_TABLE"] )
    update_expr = 'SET fullname = :fullname, address = :address, phone = :phone, avatar = :avatar'
    response = table.update_item(
        Key={ "userId":userId },
        UpdateExpression=update_expr,
        ExpressionAttributeValues={}
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        res = {"status": "ok", "msg": "profile updated"}
    else:
        res = {"status": "err", "err": "could not update profile"}
    
    return res

