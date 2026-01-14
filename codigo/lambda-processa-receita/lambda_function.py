import boto3
import json
import os
import pymysql

# Inicializa clientes AWS
s3_client = boto3.client('s3')
textract_client = boto3.client('textract')

# Configurações de banco (Amazon RDS)
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']


def lambda_handler(event, context):
    """
    Função Lambda para processar receitas médicas:
    1. Recebe evento de upload no S3
    2. Extrai texto da imagem usando Textract
    3. Insere dados no banco RDS
    """

    # Obtém informações do arquivo enviado ao S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processando arquivo: {key} do bucket: {bucket}")

    # Chama Textract para extrair texto da receita
    response = textract_client.analyze_document(
        Document={'S3Object': {'Bucket': bucket, 'Name': key}},
        FeatureTypes=["TABLES", "FORMS"]
    )

    # Extrai texto bruto
    extracted_text = ""
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + "\n"

    print("Texto extraído da receita:")
    print(extracted_text)

    # Conecta ao banco RDS
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO receitas (arquivo, texto_extraido) VALUES (%s, %s)"
            cursor.execute(sql, (key, extracted_text))
        connection.commit()
    finally:
        connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps(f"Receita {key} processada e armazenada com sucesso!")
    }
