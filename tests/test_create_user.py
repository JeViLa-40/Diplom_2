import generators
from methods.user_methods import UserMethods
import allure

class TestCreateUser:

    @allure.title('Проверка успешного создания уникального пользователя')
    def test_create_unique_user_success(self, generate_user_with_delete):
        body = generate_user_with_delete
        response = UserMethods.create_user(body)
        assert response.status_code == 200
        assert response.json()["success"] is True
        
    @allure.title('Проверка ошибки создания пользователя, который уже зарегистрирован')
    def test_cannot_create_duplicate_user(self, create_user_with_delete):
        body = create_user_with_delete
        response_dublicate = UserMethods.create_user(body)
        assert response_dublicate.status_code == 403
        assert response_dublicate.json()["message"] == 'User already exists'

    @allure.title('Проверка ошибки, если не передано обязательное поле Имя')
    def test_create_user_missing_field_error(self):
        body = generators.generate_create_user_body()
        del body['name']
        response = UserMethods.create_user(body)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
