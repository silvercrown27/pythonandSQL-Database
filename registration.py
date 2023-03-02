#  Entering Data into Users-table
from commerce_db import Users, Products, Staff


class Administration:
    def __init__(self, c):
        if c == 1:
            self.add_user()
        elif c == 2:
            self.add_product()
        elif c == 3:
            self.add_staff_member()
        else:
            print('Select the correct option..')
    def add_user(self):
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


    def add_product(self):
        try:
            prod_id = str(input('Enter Product Name : '))
            prod_name = str(input('Enter Product Name : '))
            prod_price = str(input('Enter Product Name : '))
            quantity = str(input('Enter Quantity Avalable : '))
            description = str(input('Enter Product Description : '))

            Products.create(prod_id=prod_id,
                            prod_name=prod_name,
                            prod_price=prod_price,
                            quantity=quantity,
                            description=description)

            print('user registration is a success!')

        except ValueError:
            print("Please Enter a correct value")


    def add_staff_member(self):
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


choice = int(input('Select Your Option\n 1: Add new user\n 2: Add new product\n 3: Add new staff\n'))
Administration(choice)