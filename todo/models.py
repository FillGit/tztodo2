from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import string
import random
import datetime
from datetime import datetime
from rest_framework.authtoken.models import Token

class Company(models.Model):
    name = models.CharField(max_length=50,
                            help_text="RGD, Aeroflot, Rosneft, Gazprom or empty")
    token = models.ManyToManyField(Token,
                                    blank=True,
                                    related_name="Tokens",
                                    help_text="access to company data")
    class Meta:
        permissions = (("can_work_this_obj",
                        "Work this obj. Set permission Admin"),
                      )
    
    def __str__(self):
        return self.name

class Desk(models.Model):

    company_name = models.ForeignKey('Company', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    due_date = models.DateField()
    task = models.TextField()

    executor = models.CharField(max_length=50, null=True,
                                blank=True, help_text="User executor")
    owner = models.ForeignKey('auth.User', related_name='desks',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):

        #Use the `pygments` library to create a highlighted HTML
        #representation of the code snippet.

        super(Desk, self).save(*args, **kwargs)

"""class CompanyName(models.Model):
    name = models.CharField(max_length=50,
                            help_text="RGD, Aeroflot, Rosneft, Gazprom or empty")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enabled_company = models.ManyToManyField('CompanyName',
                                             blank=True,
                                             related_name="companies",
                                             help_text="access to company data")
    date_idsession = models.DateField(null=True, blank=True)
    idsession = models.CharField(max_length=50, blank=True)
    active_company = models.CharField(max_length=50, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def before_create_profile(self, data):
        self.enabled_company.add(CompanyName.objects.get(name=data['company1']))
        self.enabled_company.add(CompanyName.objects.get(name=data['company2']))
        self.enabled_company.add(CompanyName.objects.get(name=data['company3']))
        self.enabled_company.add(CompanyName.objects.get(name=data['company4']))


class Desks(models.Model):

    company_name = models.ForeignKey('CompanyName', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    due_date = models.DateField()
    task = models.TextField()

    executor = models.CharField(max_length=50, null=True,
                                blank=True, help_text="User executor")
    owner = models.ForeignKey('auth.User', related_name='desks',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):

        #Use the `pygments` library to create a highlighted HTML
        #representation of the code snippet.

        super(Desks, self).save(*args, **kwargs)"""
