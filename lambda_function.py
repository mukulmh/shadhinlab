# Mehedy Hassan Mukul
# 07/22/22

import json

def lambda_handler(event, context):
    
    method = event['httpMethod']
    
    if method == "GET" :
        
        num1 = event['queryStringParameters']['num1']
        num2 = event['queryStringParameters']['num2']
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1+num2
            message = "Success"
        except :
            result = "NULL"
            message = "Value Error"
        
    elif method == "POST" :
        body = json.loads(event['body'])
        
        num1 = (body['num1'])
        num2 = (body['num2'])
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1+num2
            message = "Success"
        except :
            result = "NULL"
            message = "Value Error"
    
    else :
        message =  "Supported methods are GET & POST"
        result = "NULL"
        
    data = {
        "message" : message,
        "sum": result
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }