import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','recommend.settings')
import django
django.setup()


from products.models import *
from faker import Faker
from random import *
fake=Faker()

def PopulateProduct(n):
    for i in range(n):
        fid=randint(101,99999999)
        fshape=fake.random_element(elements=('Linear','Circular','Rectangular','Triangular','Spherical','Cubical','Conical','Cylindrical','Others'))
        fsize=fake.random_element(elements=('Very Small','Small','Medium','Big','Very Big','Other Size'))
        flocation=fake.city()
        fprice=randint(100,50000)
        Product_Detail=Product.objects.get_or_create(Pid=fid,shape=fshape,size=fsize,location=flocation,price=fprice)
PopulateProduct(35000)
