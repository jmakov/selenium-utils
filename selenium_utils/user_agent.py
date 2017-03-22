from selenium.webdriver.remote.webdriver import WebDriver


def get_user_agent(driver: WebDriver):
    return driver.execute_script("return navigator.userAgent")
