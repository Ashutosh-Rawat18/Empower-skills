from django.db import models

# Create your models here.


class vendors (models. Model):
    email = models.EmailField()
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=100)
    shop_service = models.CharField(max_length=20)
    phone_no = models.IntegerField(max_length=10)
