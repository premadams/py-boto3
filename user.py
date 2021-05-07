import boto3
AWS_PROFILE='mmprd'
session = boto3.session.Session(profile_name=AWS_PROFILE)

client = boto3.client('iam') 
response = client.list_users()
paginator = client.get_paginator('list_users')
for x in response['Users']:
 print (x['UserName']) 
