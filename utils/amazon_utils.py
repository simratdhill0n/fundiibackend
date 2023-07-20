import boto3
from botocore.exceptions import NoCredentialsError
from fundii_backend.settings import (
    AWS_STORAGE_BUCKET_NAME,
    AWS_S3_REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY
)

def generate_presigned_url(object_key):
    
    s3_client = boto3.client(
        's3',
        region_name=AWS_S3_REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    try:
        
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': AWS_STORAGE_BUCKET_NAME, 
                'Key': object_key,
                },
            ExpiresIn=3600
        )
        
        return presigned_url
    
    except NoCredentialsError:
        
        return None