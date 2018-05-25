# coding: utf-8 


from os import listdir
from os.path import isfile, join

import boto3

try: 
    from secret import BUCKET_NAME
except:
    from setting import BUCKET_NAME


BUCKET = BUCKET_NAME


def get_files(file_path):
    return [f for f in listdir(file_path) if isfile(join(file_path), f))]


def image_upload_to_s3(bucket, file_path, files):
    s3_client = boto3.client('s3')

    s3_objects = []

    s3_dir = 'background_image/'
    for _, f in enumerate(files):
        filename = file_path + f
        s3_key = s3_dir + f 
        
        s3_client.upload_file(filename, bucket, s3_key)
        s3_client.put_object_acl(ACL='public-read', Bucket=bucket, Key=s3_key)

        s3_objects.append(s3_key)

    return s3_objects 
    


    

