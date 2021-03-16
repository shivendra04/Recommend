import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','recommend.settings')
import django
django.setup()


from user.models import *
from faker import Faker
from random import *
fake=Faker()


def PopulateUser(n):
    for i in range(n):
        fname=fake.name()
        faddress=fake.address()
        fage=randint(5,50)
        User_Detail=User.objects.get_or_create(name=fname,age=fage,address=faddress)
PopulateUser(5)
