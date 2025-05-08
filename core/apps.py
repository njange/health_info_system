# core/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from .signals import create_roles
        post_migrate.connect(create_roles, sender=self)
