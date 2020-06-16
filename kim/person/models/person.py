from django.db import models
from django.forms import DateField


class Person (models.Model):
    date_last_change = models.DateField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=5, choices= [
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),
    ])
    email = models.EmailField(max_length=254)
    phone = models.TextField(max_length=10)
    phone_mob = models.TextField(max_length=10)
    birth_date = models.DateTimeField(auto_now=False, auto_now_add=False)
