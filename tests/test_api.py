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



@allure.feature("API Testing")
@allure.story("Create new post")
def test_create_post(page):
    # Данные, которые мы хотим отправить на сервер
    new_post = {
        "title": "Gemini & Dmitrij",
        "body": "Automation is power",
        "userId": 1
    }
    
    # 1. Отправляем POST запрос с данными (data)
    response = page.request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=new_post
    )
    
    # 2. Проверяем статус 201 (Created — стандарт для успешного создания)
    assert response.status == 201
    
    # 3. Проверяем, что сервер вернул наши данные и присвоил ID
    result = response.json()
    assert result["title"] == new_post["title"]
    assert "id" in result
    print(f"Created post ID: {result['id']}")

@allure.feature("API Testing")
@allure.story("Delete post")
def test_delete_post(page):
    # 1. Отправляем DELETE запрос на конкретный ID (например, 1)
    response = page.request.delete("https://jsonplaceholder.typicode.com/posts/1")
    
    # 2. Проверяем статус 200 или 204 (No Content)
    # JSONPlaceholder возвращает 200
    assert response.status == 200
    print("Post deleted successfully")