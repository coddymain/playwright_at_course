import pytest
import allure

from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    # Создаем объект страницы один раз для всех тестов
    return LoginPage(page)



# Эта фикстура будет срабатывать после каждого теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        page = item.funcargs['page']
        allure.attach(
            page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )