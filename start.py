from config import *


def centos():
    ec2 = boto3.resource('ec2', region_name="eu-north-1")
    outfile = open('virtualkacentoss.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName='virtualkacentoss')
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
        "1. Вивiд всiх бакетiв 2. Вивiд бакета 3. Завантажити 4. Скачати 5. Створити віртуалку  6. Видалити віртуалку 7. Список віртуалок 8. Вихiд = > "))

    if q == 1:
        show_all_bucket()

    elif q == 2:
        view_bucket()

    elif q == 3:
        upload_bucket()

    elif q == 4:
        dowload_bucket()

    elif q == 5:
        create_instance()

    elif q == 6:
        Delete()

    elif q == 7:
        show()

    elif q == 8:
        break
