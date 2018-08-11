import boto3
ec2= boto3.client('ec2',region_name= 'us-east-1')
response = ec2.describe_instances()
for x in response['Reservations']:
    a = x['Instances'][0]['ImageId']
    b = x['Instances'][0]['InstanceId']
    c = x['Instances'][0]['InstanceType']
    for y in x['Instances']:
        d = y['Tags'][1]['Value']
        e = y['State']['Name']
        print(e)
        print("Instance with instance id is {}, Instance type is {}, name is {}, and its state is {}".format(b,c,d,e))
