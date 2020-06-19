from config import *


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


while True:

    q = int(input(
        "1. Вивiд всiх бакетiв 2. Вивiд бакета 3. Завантажити 4. Скачати 5. Создать виртуалку 6. Вихiд = > "))

    if q == 1:
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            print(bucket.name)

    elif q == 2:
        view = input('Вивiд бакета = > ')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(view)
        for text in bucket.objects.all():
            print(text.key)

    elif q == 3:
        your_bucket = input("Бакет = >")
        file_name = input("Iм'я файла > ")
        s3 = boto3.client('s3')
        s3.upload_file(file_name, your_bucket, file_name)

    elif q == 4:
        your_bucket = input(" Бакет = >")
        file_name = input("Iм'я файла > ")
        s3 = boto3.client('s3')
        s3.download_file(your_bucket, file_name, file_name)
    elif q == 5:
        choise = int(input("1. Centos 2. Ubuntu"))
        if choise == 1:
            centos()
        elif choise == 2:
            ubuntu()
    elif q == 6:
        break
