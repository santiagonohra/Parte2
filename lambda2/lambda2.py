#Santiago Nohra
import json
import boto3
from datetime import datetime
import time
import ast

def lambda_handler(event, context):
   
   
   
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('dolarraw')
   
    obj = bucket.Object('dolar_{}.txt'.format(datetime.fromtimestamp(time.time()).date()))
   
    body = obj.get()['Body'].read()
   
    data = body.decode()
    data = ast.literal_eval(data)
   
    data_to_upload= 'fechahora, valor'
   
    for dato in data:
        data_to_upload += '\n'+str(datetime.fromtimestamp(int(dato[0])/1000))+','+dato[1]
   
    s3 = boto3.resource('s3')
    object = s3.Object('dolarclean', 'dolar_{}.csv'.format(datetime.fromtimestamp(time.time()).date()))
    object.put(Body=data_to_upload)
   
    return {
        'statusCode': 200,
        'body': json.dumps('Csv data updated')
    }

