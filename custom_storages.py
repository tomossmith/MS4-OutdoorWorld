""" Settings for Storage Locations """
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ static storage location """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ media storage location """
    location = settings.MEDIAFILES_LOCATION
