from storages.backends.s3boto3 import S3Boto3Storage
from . import settings

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_MAIN_BUCKET_NAME
    location = 'static'

class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_TEMP_BUCKET_NAME
    location = 'media'
    default_acl = 'private'
    file_overwrite = False