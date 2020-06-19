from boto3.session import Session
import boto3

ACCESS_KEY = 'AKIAT5NIZR6LCEYXTPB7'
SECRET_KEY = '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'

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)


def centos():
    ec2 = boto3.resource('ec2', region_name="eu-north-1")
    outfile = open('v_centos.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName='v_centos')
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)

    instances = ec2.create_instances(
        ImageId='ami-0334fa6d0c950747c',
        MinCount=1,
        MaxCount=1,
        KeyName="v_centos",
        InstanceType="t3.micro"
    )


def ubuntu():
    ec2 = boto3.resource('ec2', region_name="eu-north-1")
    outfile = open('v_ubuntu.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName='v_ubuntu')
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)

    instances = ec2.create_instances(
        ImageId='ami-0caae0b310f01ff33',
        MinCount=1,
        MaxCount=1,
        KeyName="v_ubuntu",
        InstanceType="t3.micro"
    )


def show():
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print("ID = ", instance["InstanceId"])
            print("PublicDNS = ", instance["PublicDnsName"])
            print("Public IP  = ", instance.get('PublicIpAddress'))
            print("InstanceType =", instance["InstanceType"])
            print("State = ", instance["State"])
            print("Key = ", instance["KeyName"])
            print("\n")


def show_all_bucket():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def view_bucket():
    view = input('Вивiд бакета = > ')
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(view)
    for text in bucket.objects.all():
        print(text.key)


def upload_bucket():
    your_bucket = input("Бакет = >")
    file_name = input("Iм'я файла > ")
    s3 = boto3.client('s3')
    s3.upload_file(file_name, your_bucket, file_name)


def dowload_bucket():
    your_bucket = input(" Бакет = >")
    file_name = input("Iм'я файла > ")
    s3 = boto3.client('s3')
    s3.download_file(your_bucket, file_name, file_name)


def Delete():
    ids = []
    add = input("ID віртуалкі => ")
    ids.append(add)
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=ids).terminate()


def create_instance():
    choise = int(input("1. Centos 2. Ubuntu "))
    if choise == 1:
        centos()
    elif choise == 2:
        ubuntu()
