from boto3.session import Session
import boto3

ACCESS_KEY = ''
SECRET_KEY ='

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)


def centos():
    ec2 = boto3.resource('ec2', region_name="eu-north-1")
    outfile = open('virtualkacentos.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName='virtualkacentos')
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)

    instances = ec2.create_instances(
        ImageId='ami-0334fa6d0c950747c',
        MinCount=1,
        MaxCount=1,
        KeyName="virtualkacentos",
        InstanceType="t3.micro"
    )


def ubuntu():
    ec2 = boto3.resource('ec2', region_name="eu-north-1")
    outfile = open('virtualkaubuntu.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName='virtualkaubuntu')
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)

    instances = ec2.create_instances(
        ImageId='ami-0caae0b310f01ff33',
        MinCount=1,
        MaxCount=1,
        KeyName="virtualkaubuntu",
        InstanceType="t3.micro"
    )
