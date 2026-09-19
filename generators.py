from faker import Faker

fake = Faker()

def generate_create_user_body():
    body = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
    return body
