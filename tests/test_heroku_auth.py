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
    