import os
from dotenv import load_dotenv
from playwright.sync_api import expect
import pytest

# 1. Загружаем секреты из .env
load_dotenv()

def test_successful_login(login_page):
    """Тест успешного входа с использованием скрытых учетных данных"""
    # Берем данные из файла .env
    user = os.getenv("HEROKU_USER")
    password = os.getenv("HEROKU_PASSWORD")
    
    login_page.navigate()
    login_page.login(user, password)
    
    expect(login_page.flash_message).to_contain_text("You logged into a secure area!")

@pytest.mark.parametrize("username, password, expected_error", [
    ("invalid_user", "wrong_pass", "Your username is invalid!"),
    ("tomsmith", "wrong_password", "Your password is invalid!"),
])
def test_negative_logins(login_page, username, password, expected_error):
    """Параметризованный тест для проверки ошибок входа"""
    login_page.navigate()
    login_page.login(username, password)
    
    expect(login_page.flash_message).to_contain_text(expected_error)