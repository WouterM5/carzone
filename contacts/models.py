from datetime import datetime
from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=255)
    car_title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    user_id = models.CharField(max_length=1000,blank=True)
    create_date = models.DateTimeField(blank=True, default = datetime.now)

    def __str__(self):
        return self.email

class Form(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default = datetime.now)

    def __str__(self):
        return self.email