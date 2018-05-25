# coding: utf-8 


import boto3

try: 
    from secret import BUCKET_NAME
except:
    from setting import BUCKET_NAME


BUCKET = BUCKET_NAME


