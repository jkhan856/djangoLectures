import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','show_DB_content.settings')

import django
django.setup()

##Fake POP script

import random
from users.models import UserInfo
from faker import Faker

fakegen = Faker()

def populate(n=10):
    for entry in range(n):
        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name()
        fake_email = fakegen.email()

        user = UserInfo.objects.get_or_create(first_name = fake_firstName, last_name = fake_lastName, email = fake_email)[0]
        user.save()

if __name__ == '__main__':
    print('Populating script')
    populate(10)
    print("Populating Completed!")
