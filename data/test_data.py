import os

from faker import Faker
fake = Faker()

class Data:
    f_name = fake.first_name()
    email = fake.email()
    password = fake.password()
    month = fake.month_name()
    l_name = fake.last_name()
    company = fake.company()
    address1 = fake.address()
    address2 = fake.administrative_unit()
    country = "United States"
    state = fake.state()
    city = fake.city()
    zipcode = fake.zipcode()
    mobile = fake.phone_number()
    name = fake.name()
    subj = fake.word()
    message = fake.word()
    product_name = 'cotton'
    first_product_url = "https://www.automationexercise.com/product_details/1"


