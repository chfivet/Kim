from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class PersonAdmin(admin.ModelAdmin):
    list_display = ('changed', 'email', 'first_name', 'last_name', 'middle_name', 'user')
    search_fields = ['email', 'first_name', 'last_name', 'middle_name', 'user__username']
    raw_id_fields = ['user']


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

    def __str__(self):
        if self.middle_name:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)

    def username(self):
        if self.user is None:
            return None
        return self.user.username
