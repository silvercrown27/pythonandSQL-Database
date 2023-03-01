from commerce_db import Users, Products, Staff

users = Users.select()
products = Products.select()
staff = Staff.select()


def view_users():
    for user in users:
        print(user.user_id, user.user_name, user.user_email, user.location, user.contact)


def view_products():
    for product in products:
        print(product.prod_id, product.prod_name, product.prod_price, product.quantity, product.description)


def view_staff_members():
    for member in staff:
        print(member.member_id, member.member_name, member.member_age)


view_users()
