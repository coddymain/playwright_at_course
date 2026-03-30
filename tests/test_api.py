import allure
from playwright.sync_api import APIRequestContext

@allure.feature("API Testing")
@allure.story("Get user details")
def test_get_user(page):
    # 1. Отправляем GET запрос на сервер
    # Мы используем контекст запроса из текущей страницы или создаем новый
    response = page.request.get("https://jsonplaceholder.typicode.com/users/1")
    
    # 2. Проверяем, что статус ответа 200 (успех)
    assert response.status == 200
    
    # 3. Распаковываем JSON (данные, которые прислал сервер)
    user_data = response.json()
    
    # 4. Проверяем конкретные данные пользователя
    assert user_data["username"] == "Bret"
    assert "email" in user_data
    
    print(f"User email is: {user_data['email']}")