from django.contrib.auth.models import User
from django.db import models


class Person (models.Model):
    birth_date = models.DateField(auto_now=False, null=True)
    changed = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    last_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.TextField(max_length=30, null=True)
    phone_mob = models.TextField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
