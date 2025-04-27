from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    programs = models.ManyToManyField(Program, related_name='clients', blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_group')

    def __str__(self):
        return self.username
    def get_roles(self):
        return [group.name for group in self.groups.all()]
  