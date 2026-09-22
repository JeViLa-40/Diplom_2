import requests
import allure
from data import Url

class UserMethods:
    @staticmethod
    def create_user(body):
        with allure.step('Создание пользователя'):
            return requests.post(url=Url.REGISTER_ENDPOINT, json=body)
            
    @staticmethod
    def delete_user(access_token):
        with allure.step('Удаление пользователя'):
            return requests.delete(url=Url.DELETE_USER_ENDPOINT, headers={'Authorization': access_token})

    @staticmethod
    def login_user(email, password):
        body = {
            "email": email,
            "password": password
        }
        with allure.step('Авторизация пользователя'):
            return requests.post(url=Url.LOGIN_ENDPOINT, json=body)
