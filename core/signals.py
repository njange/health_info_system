# core/signals.py
from django.contrib.auth.models import Group

def create_roles(sender, **kwargs):
    roles = ['Admin', 'Doctor', 'Nurse']
    for role in roles:
        Group.objects.get_or_create(name=role)