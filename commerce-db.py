from os import path
from peewee import *

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join("e-commerce"))


class Staff(Model):
    member_id = CharField()
    member_name = CharField()
    member_age = CharField()

    class Meta:
        database = db


class Products(Model):
    prod_id = CharField()
    prod_name = CharField()
    prod_price = IntegerField()
    quantity = IntegerField()
    description = CharField()

    class Meta:
        database = db


class Users(Model):
    user_name = CharField()
    user_email = CharField()
    location = CharField()
    contact = IntegerField()

    class Meta(Model):
        database = db


Staff.create_table(fail_silently=True)
Products.create_table(fail_silently=True)
Users.create_table(fail_silently=True)
