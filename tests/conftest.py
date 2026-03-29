import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    # Создаем объект страницы один раз для всех тестов
    return LoginPage(page)