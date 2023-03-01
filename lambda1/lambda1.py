#Santiago Nohra
import json
from urllib.request import urlopen
import boto3
import time
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    with urlopen("https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario") as response:
        body = response.read()
   
    raw_data = json.loads(body.decode('utf-8'))
   
   
   
   
   
   
    s3 = boto3.resource('s3')
    object = s3.Object('dolarraw', 'dolar_{}.txt'.format(datetime.fromtimestamp(time.time()).date()))
    object.put(Body=str(raw_data))
   
   
    return {
        'statusCode': 200,
        'body': json.dumps('Archivos subidos')
    }