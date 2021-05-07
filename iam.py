import datetime, boto3, csv

session = boto3.session.Session(profile_name='matchmove')
IAM = session.client("iam")
def access_key(user):
       file1 = open('matchmove.txt', 'r')
       Lines = file1.readlines()
       for user in Lines:
     #   print(user)
        keydetails=IAM.list_access_keys(UserName=user.strip())
        for keys in keydetails['AccessKeyMetadata']:
            if keys['Status']=='Active' and (time_diff(keys['CreateDate'])) >=90:
                keydeatils=IAM.update_access_key(
                UserName=user.strip(),
                AccessKeyId=keys['AccessKeyId'],
                Status='Inactive'
               )
                print (keys['UserName'],keys['AccessKeyId'], time_diff(keys['CreateDate']))
def time_diff(keycreatedtime):
    now=datetime.datetime.now(datetime.timezone.utc)
    diff=now-keycreatedtime
    return diff.days
if __name__ == '__main__':
    details = IAM.list_users(MaxItems=300)
    print ("Username","AccessKey","KeyAge")
    for user in details['Users']:
        access_key(user['UserName'])
