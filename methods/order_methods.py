import requests
import allure
from data import Url

class OrderMethods:
    @staticmethod
    def make_order(body, headers=None):
        with allure.step('Создание заказа'):
            return requests.post(url=Url.MAKE_ORDER_ENDPOINT, headers=headers, json=body)
