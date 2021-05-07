import boto3

iam = boto3.client('iam')

def find_user_and_groups():
    for userlist in iam.list_users()['Users']:
        
        print("Username: "  + userlist['UserName'])
