def lambda_handler(event, context):
    
    print(event)
    
    if event['authorizationToken'] == 'customtoken':
        auth = 'Allow'
    else:
        auth = 'Deny'
    
    authResponse = { "principalId": "customtoken", "policyDocument": { "Version": "2012-10-17", "Statement": [{"Action": "execute-api:Invoke", "Resource": ["arn:aws:execute-api:ca-central-1:618758721119:jk8ikfnt3i/*/*"], "Effect": auth}] }}
    return authResponse