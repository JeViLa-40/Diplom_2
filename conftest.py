import pytest
from methods.user_methods import UserMethods
import generators

@pytest.fixture
def create_user_with_delete():
    body = generators.generate_create_user_body()
    response = UserMethods.create_user(body)

    yield {
        'body': body, 
        'response': response
    }

    UserMethods.delete_user(response.json()['accessToken'])

@pytest.fixture
def login_user(create_user_with_delete):
    body = create_user_with_delete['body']
    response = UserMethods.login_user(body['email'], body['password'])
    return response.json()['accessToken']
 
