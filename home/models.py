from django.db import models

# Create your models here
class ContactModel(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    message=models.TextField()

class AddressModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.TextField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip=models.IntegerField()

class PaymentModel(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    expiration=models.TextField()
    cvv=models.IntegerField()