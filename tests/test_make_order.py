from methods.order_methods import OrderMethods
import allure

class TestMakeOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_make_order_success_with_auth(self, login_user):
        accessToken = login_user
        body = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        }
        headers = {'Authorization': accessToken}
        response = OrderMethods.make_order(body, headers)
        assert response.status_code == 200
        assert response.json()["order"]["number"]

    @allure.title('Проверка создания заказа без авторизациии') #По требованиям только авторизованный пользователь может создавать заказ
    def test_make_order_error_without_auth(self):
        body = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        }
        response = OrderMethods.make_order(body)
        assert response.status_code == 403

    @allure.title('Проверка ошибки создания заказа без ингредиентов')
    def test_make_order_error_without_ingredients(self, login_user):
        accessToken = login_user
        body = {
            "ingredients": []
        }
        headers = {'Authorization': accessToken}
        response = OrderMethods.make_order(body, headers)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверка ошибки создания заказа c невалидным хешом ингредиента')
    def test_make_order_error_with_invalid_ingredient_hash(self, login_user):
        accessToken = login_user
        body = {
            "ingredients": ["60"]
        }
        headers = {'Authorization': accessToken}
        response = OrderMethods.make_order(body, headers)
        assert response.status_code == 500
