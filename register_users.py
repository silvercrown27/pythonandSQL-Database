#  Entering Data into Users-table

from commerce_db import Users

try:
    user_name = str(input('Enter Your Name : '))
    user_email = str(input('Enter Your Email : '))
    location = str(input('Enter Your Current Location : '))
    contact = str(input('Enter Your Contact Info : '))

    Users.create(user_name=user_name, user_email=user_email,
                 location=location, contact=contact)
    print('user registration is a success!')

except ValueError:
    print("Please Enter a correct value")
