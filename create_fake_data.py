# create_fake_data.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userprofile_project.settings')

import django
django.setup()

from django_seed import Seed
from userprofile_app.models import UserProfile

seeder = Seed.seeder()

def generate_fake_data(num_profiles=25):
    seeder.add_entity(UserProfile, num_profiles, {
        'name': lambda x: seeder.faker.name(),
        'designation': lambda x: seeder.faker.job(),
        'company': lambda x: seeder.faker.company(),
        'about': lambda x: seeder.faker.paragraph(),
        'areas_of_interest': lambda x: seeder.faker.words(nb=10),  # Adjust the number of words as needed
    })
    seeder.execute()

if __name__ == '__main__':
    generate_fake_data()

