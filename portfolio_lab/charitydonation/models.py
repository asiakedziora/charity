from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=128)


TYPES = [
    ('F', 'fundacja'),
    ('OPZ', 'organizacja pozarządowa'),
    ('ZL', 'zbiórka lokalna'),
]


class Institution(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    description = models.CharField(max_length=128)
    type = models.CharField(choices=TYPES, default='F', max_length=3)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=128) #charfield
    zip_code = models.CharField(max_length=6) #regex walidacja
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)




