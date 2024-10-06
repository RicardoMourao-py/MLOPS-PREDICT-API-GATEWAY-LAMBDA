# MlOps APS03

## Dependências
- Ubuntu
- Docker
- AWS CLI
- Python

## Autentica AWS
```bash
# Configure as credenciais
$ aws configure --profile mlops

>> AWS Access Key ID [None]: 
>> AWS Secret Access Key [None]:
>> Default region name [None]: 
>> Default output format [None]:

# Exporta profile
$ export AWS_PROFILE=mlops
```

## Criando Ambiente

```bash
$ python3 -m venv mlops
$ source ./mlops/bin/activate
```

## Clonando o projeto

```bash
$ git clone https://github.com/insper-classroom/24-2-mlops-aps03-RicardoMourao-py.git

$ pip install -r requirements.txt
```

## Testando Localmente
```bash
$ docker build --platform linux/amd64 -t aps03:main .

$ docker run -p 9500:8080 aps03:main

$ curl "http://localhost:9500/2015-03-31/functions/function/invocations" -d '{}'
```

## Subindo Infraestrutura
```bash
$ repository_name="aps03_ricardomrf"

$ aws ecr create-repository \
    --repository-name "$repository_name" \
    --image-scanning-configuration scanOnPush=true \
    --image-tag-mutability MUTABLE \
    --query 'repository.{repositoryArn:repositoryArn, repositoryUri:repositoryUri}' \
    --output text

$ aws ecr get-login-password --region us-east-2 --profile mlops | docker login --username AWS --password-stdin 820926566402.dkr.ecr.us-east-2.amazonaws.com

$ docker tag aps03:main 820926566402.dkr.ecr.us-east-2.amazonaws.com/aps03_ricardomrf:latest

$ docker push 820926566402.dkr.ecr.us-east-2.amazonaws.com/aps03_ricardomrf:latest

$ python3 create_lambda_function.py 
$ python3 invoke_lambda_function.py 
$ python3 create_api_gateway.py

>> API Endpoint: https://2a2sukbr3f.execute-api.us-east-2.amazonaws.com
```