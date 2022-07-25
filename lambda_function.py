# Mehedy Hassan Mukul
# 07/22/22

import json

def lambda_handler(event, context):
    
    method = event['httpMethod']
    
    if method == "GET" :
        
        try:
            num1 = float(event['queryStringParameters']['num1'])
            num2 = float(event['queryStringParameters']['num2'])
            result = num1+num2
            message = "Success"

        except:
            try:
                num1 = float(event['queryStringParameters']['num1'])
            except:
                message ="num1 param must be numeric"
            try:
                num2 = float(event['queryStringParameters']['num2'])
            except:
                message ="num2 param must be numeric"

            result = "NULL"
                
        
    elif method == "POST" :
        body = json.loads(event['body'])
        
        num1 = (body['num1'])
        num2 = (body['num2'])
        result = num1+num2
        message = "Success"

    
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
