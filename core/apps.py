from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth.models import Group  # Import here to avoid AppRegistryNotReady
        roles = ['Admin', 'Doctor', 'Nurse']
        for role in roles:
            Group.objects.get_or_create(name=role)