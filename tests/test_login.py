from methods.user_methods import UserMethods
import allure

class TestLogin:

    @allure.title('Проверка успешной авторизации существующего пользователя')
    def test_login_user_success(self, create_user_with_delete):
        body = create_user_with_delete
        response = UserMethods.login_user(body['email'], body['password'])
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка ошибки авторизации пользователя с неверным логином')
    def test_login_fails_with_invalid_email(self, create_user_with_delete):
        body = create_user_with_delete
        response = UserMethods.login_user('rhp@nano.ru', body['password'])
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
