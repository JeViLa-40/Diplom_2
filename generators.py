from faker import Faker

fake = Faker()

def generate_create_user_body():

    username = fake.pystr(min_chars=10, max_chars=15)
    domain = fake.free_email_domain()

    email = f"{username}@{domain}"

    body = {
        "email": email,
        "password": fake.password(),
        "name": fake.name()
    }
    return body
