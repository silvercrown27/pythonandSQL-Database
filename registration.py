#  Entering Data into Users-table
from commerce_db import Users, Products, Staff


def add_user():
    try:
        user_id = str(input('Enter Enter ID : '))
        user_name = str(input('Enter Your Name : '))
        user_email = str(input('Enter Your Email : '))
        location = str(input('Enter Your Current Location : '))
        contact = str(input('Enter Your Contact Info : '))

        Users.create(user_id=user_id,
                     user_name=user_name,
                     user_email=user_email,
                     location=location,
                     contact=contact)

        print('user registration is a success!')

    except ValueError:
        print("Please Enter a correct value")


def add_product():
    try:
        prod_id = str(input('Enter Your Name : '))
        prod_name = str(input('Enter Your Name : '))
        prod_price = str(input('Enter Your Name : '))
        quantity = str(input('Enter Your Name : '))
        description = str(input('Enter Your Name : '))

        Products.create(prod_id=prod_id,
                        prod_name=prod_name,
                        prod_price=prod_price,
                        quantity=quantity,
                        description=description)

        print('user registration is a success!')

    except ValueError:
        print("Please Enter a correct value")


def add_staff_member():
    try:
        member_id = str(input('Enter Staff ID : '))
        member_name = str(input('Enter Staff Name : '))
        member_age = str(input('Enter Staff AGe : '))

        Staff.create(member_id=member_id,
                     member_name=member_name,
                     member_age=member_age)
        print('user registration is a success!')

    except ValueError:
        print("Please Enter a correct value")


add_user()
