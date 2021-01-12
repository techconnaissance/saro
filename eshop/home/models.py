from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    message = models.CharField(max_length=2083)
    is_addressed = models.BooleanField()
    added_date = models.DateTimeField()
    added_by = models.CharField(max_length=50)
    updated_date = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
