from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserModel(models.Model):
    UserName=models.CharField(max_length=200)
    Email = models.EmailField()
    Mobile =models.CharField(max_length=20)
    Password=models.CharField(max_length=255)
    # image field

    def __str__(self):
        return self.UserName
