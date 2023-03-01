from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "sql-basics.db"))


#  Creating our first table
class Student(Model):
    stud_name = CharField()
    stud_id = CharField()
    stud_age = IntegerField()
    stud_email = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)
