import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Provide function name: "ex_docker_<INSPER_USERNAME>"
function_name = "aps03_ricardomrf"

# Provide Image URI from before
image_uri = "820926566402.dkr.ecr.us-east-2.amazonaws.com/aps03_ricardomrf:latest"

lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# # Atualizar configuração da função Lambda
# response = lambda_client.update_function_configuration(
#     FunctionName=function_name,
#     Timeout=60,  # Novo timeout (em segundos)
#     MemorySize=256,  # Nova quantidade de memória (em MB)
# )

response = lambda_client.create_function(
    FunctionName=function_name,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Role=lambda_role_arn,
    Timeout=60,  # Optional: function timeout in seconds
    MemorySize=256,  # Optional: function memory size in megabytes
)

print("Lambda function created successfully:")
print(f"Function Name: {response['FunctionName']}")
print(f"Function ARN: {response['FunctionArn']}")