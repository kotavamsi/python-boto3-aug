import boto3
ec2 = boto3.client('ec2',region_name = 'us-west-2')
res = ec2.run_instances(
                        ImageId = 'ami-0ad99772',
                        InstanceType = 't2.micro',
                        MaxCount=1,
                        MinCount=1
                           )
print(res)