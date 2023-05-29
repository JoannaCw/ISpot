from faker import Faker
class Invaliddata():
    f=Faker("pl-PL")
    email=f.email()
    password=f.password(8)
    name=f.first_name()
    last_name=f.last_name()



