from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(username=os.getenv("username"), password=os.getenv("password"))

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0
test_login_page(browser)
browser.close()