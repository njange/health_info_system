from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create a new doctor user and assign them to the Doctor group'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the doctor')
        parser.add_argument('email', type=str, help='Email address')
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"User '{username}' already exists."))
            return

        user = User.objects.create_user(username=username, email=email, password=password)
        group, created = Group.objects.get_or_create(name='Doctor')
        user.groups.add(group)
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Doctor user '{username}' created and added to 'Doctor' group."))
