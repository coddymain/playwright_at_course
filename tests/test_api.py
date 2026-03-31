import allure
import pytest
from playwright.sync_api import Page, expect

@allure.feature("API Testing")
@allure.story("Get multiple users (Parametrized)")
@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
])
def test_get_multiple_users(page: Page, user_id, expected_name):
    """Проверяем получение данных разных пользователей по ID"""
    response = page.request.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    assert response.status == 200
    user_data = response.json()
    assert user_data["name"] == expected_name

@allure.feature("API Testing")
@allure.story("Create and Delete Post")
def test_post_lifecycle(page: Page):
    """Проверяем создание поста и его последующее удаление (Жизненный цикл)"""
    
    # 1. Создание (POST)
    new_post = {"title": "API Master", "body": "Learning Playwright", "userId": 1}
    create_res = page.request.post("https://jsonplaceholder.typicode.com/posts", data=new_post)
    assert create_res.status == 201
    post_id = create_res.json()["id"]
    
    # 2. Удаление (DELETE)
    delete_res = page.request.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert delete_res.status == 200