import json
import time
import boto3
import os

'''
# DEMO EVENT
{
  "userName": "<UUID>",
  "version": "1",
  "userPoolId": "xxxxxx",
  "callerContext": {
    "awsSdkVersion": "xxxxxxxxx",
    "clientId": "xxxxxxxxxxxxx"
  },
  "region": "<AWS_REGION>",
  "request": {
    "userAttributes": {
      "phone_number": "+1123123123123",
      "sub": "<UUID, same as userName>",
      "phone_number_verified": "false",
      "cognito:email_alias": "<EMAIL>",
      "cognito:user_status": "CONFIRMED",
      "email_verified": "true",
      "email": "<EMAIL, smae as above>"
    }
  },
  "response": {},
  "triggerSource": "PostConfirmation_ConfirmSignUp"
}
'''

'''
def add_admin_user(userId):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("DVSA-ADMIN-DB")
    response = table.put_item(
        Item={
            'userId': userId
        }
    )
    return {"status": "ok", "msg": response}
'''

def lambda_handler(event, context):

    userId = event["userName"]
    ts = int(time.time())

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table( os.environ["USERS_TABLE"] )
    response = table.put_item(
       Item={
            'userId': userId
        }
    )

    invokeLambda = boto3.client('lambda')
    payload = {"action": "verify", "user": userId }
    invokeLambda.invoke(FunctionName='DVSA-USER-INBOX', InvocationType='Event', Payload=json.dumps(payload))

    '''
    FAKE CODE CAN GO HERE
    '''


    return event

