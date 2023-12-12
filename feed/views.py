from django.shortcuts import render

# Create your views here.

#create new post, 

''' 
per day max number of posts
AWS S3 Bucket Policy for size,
if already sent presigned url for the user, and not yet uploded and sent back the uploaded url, give the same presigned url
'''

# import boto3
# from django.conf import settings
# from django.http import JsonResponse

# def generate_presigned_url(request):
#     s3_client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
#     bucket_name = 'your-bucket-name'
#     object_name = 'desired-object-name-in-s3'
#     presigned_url = s3_client.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=3600)
#     return JsonResponse({'url': presigned_url})

