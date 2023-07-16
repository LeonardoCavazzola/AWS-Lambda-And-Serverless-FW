import json
import boto3
from awslambdaric.lambda_context import LambdaContext

dynamodb = boto3.resource('dynamodb', 'us-east-1')
table = dynamodb.Table('people')


def build_headers() -> dict:
    return {
        'Content-Type': 'application/json'
    }


def build_response(status: int, headers: dict, body: dict = None) -> dict:
    response = {
        'statusCode': status,
        'headers': headers,
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response


def put_person(event: dict, context: LambdaContext) -> dict:
    email = event['pathParameters']['email']
    person = json.loads(event['body'])
    person['email'] = email
    table.put_item(Item=person)
    return build_response(
        status=201,
        headers=build_headers(),
        body=person,
    )


def get_person(event: dict, context: LambdaContext) -> dict:
    email = event['pathParameters']['email']
    item_response = table.get_item(
        Key={
            'email': email
        }
    )

    try:
        item = item_response['Item']
        return build_response(
            status=200,
            headers=build_headers(),
            body=item,
        )
    except KeyError:
        return build_response(
            status=404,
            headers=build_headers()
        )
