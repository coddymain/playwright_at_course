from playwright.sync_api import Page, expect


# В Pytest мы просто передаем 'page' в аргументы. 
# Pytest сам откроет браузер, создаст страницу и закроет её после теста!
def test_successful_login(page: Page):
    # 1. Переходим на страницу
    page.goto("https://the-internet.herokuapp.com/login")
        
    # 2. Вводим данные (используем локаторы из твоего черновика)
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    
    # 3. Нажимаем кнопку Login
    page.get_by_role("button", name=" Login").click()
    
    # 4. ПРОФЕССИОНАЛЬНЫЙ ШАГ: Проверка (Assertion)
    # Мы ожидаем, что на странице появится текст об успешном входе
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()

    
    # Нажимаем на кнопку выхода, которую мы только что обсудили
    page.get_by_role("link", name="Logout").click()
    # Проверяем, что снова видим заголовок страницы входа
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()
    
def test_failed_login(page: Page):
    # 1. Переходим на страницу
    page.goto("https://the-internet.herokuapp.com/login")

    # 2. Вводим неправильные данные
    page.get_by_role("textbox", name="Username").fill("wrong_user")
    page.get_by_role("textbox", name="Password").fill("wrong_password")
    # 3. Нажимаем кнопку Login
    page.get_by_role("button", name=" Login").click()
    # 4. Проверяем, что отображается сообщение об ошибке
    # Мы используем id="flash" для локатора, так как это уникальный идентификатор для этого сообщения
    error_message = page.locator("#flash")
    expect(error_message).to_contain_text("Your username is invalid!")
        
def test_empty_fields_login(page: Page):
    # 1. Переходим на страницу
    page.goto("https://the-internet.herokuapp.com/login")

    # 2. Оставляем поля пустыми и нажимаем кнопку Login
    page.get_by_role("button", name=" Login").click()
    
    # 3. Проверяем, что отображается сообщение об ошибке для пустых полей
    error_message = page.locator("#flash")
    expect(error_message).to_contain_text("Your username is invalid!") 