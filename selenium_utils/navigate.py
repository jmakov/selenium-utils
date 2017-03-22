from selenium.webdriver.remote.webdriver import WebDriver


def scroll_to(driver: WebDriver, y: str):
    driver.execute_script("window.scrollTo(0, {});".format(y))


def scroll_to_page_bottom(driver: WebDriver):
    """Scrolls to te page bottom using JS
    Args:
        driver (base.CustomDriver)
    """
    scroll_to(driver, "document.body.scrollHeight)")
