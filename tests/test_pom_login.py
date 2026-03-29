from playwright.sync_api import Page, expect


def test_login_with_pom_fixture(login_page):
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(login_page.flash_message).to_contain_text("You logged into a secure area!")
    