import random
from faker import Faker
from core.models import Program, Client, User
from django.contrib.auth.models import Group

fake = Faker()

def populate_programs(n=10):
    """Create n dummy programs."""
    programs = []
    for _ in range(n):
        program_name = fake.unique.word().capitalize()
        programs.append(Program(name=program_name))
    Program.objects.bulk_create(programs)
    print(f"Created {n} programs.")

def populate_users(n=100):
    """Create n dummy users."""
    users = []
    for _ in range(n):
        username = fake.unique.user_name()
        email = fake.unique.email()
        password = fake.password(length=10)
        users.append(User(username=username, email=email, password=password))
    User.objects.bulk_create(users)
    print(f"Created {n} users.")

def populate_clients(n=1000):
    """Create n dummy clients and assign them to random programs."""
    programs = list(Program.objects.all())
    clients = []
    for _ in range(n):
        name = fake.name()
        age = random.randint(18, 80)
        contact = fake.phone_number()
        client = Client(name=name, age=age, contact=contact)
        client.save()  # Save first to create ManyToMany relationships
        client.programs.set(random.sample(programs, random.randint(1, min(3, len(programs)))))
        clients.append(client)
    print(f"Created {n} clients.")

def run():
    print("Populating database with dummy data...")
    populate_programs(10)  # Create 10 programs
    populate_users(100)    # Create 100 users
    populate_clients(1000) # Create 1000 clients
    print("Database population complete.")