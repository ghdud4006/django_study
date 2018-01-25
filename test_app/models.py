from django.db import models
from django.utils import timezone

class testmodel(models.Model):
    model_ID = models.CharField(max_length=12)
    model_NAME = models.CharField(max_length=20)
    model_PASSWORD = models.CharField(max_length=32)
    