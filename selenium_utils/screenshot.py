from selenium.webdriver.remote.webdriver import WebDriver


def resize_to_page_size(driver: WebDriver):
    """
    Resizes the window to the size of the whole web page

    Details:
    Copied from https://gist.github.com/elcamino/5f562564ecd2fb86f559
    """
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, "
        "document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight,"
        " document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(width + 100, height + 100)


def get_screenshot(driver: WebDriver, file_name: str):
    """Gets the screenshot of the whole web page"""
    resize_to_page_size(driver)
    driver.get_screenshot_as_file(file_name)
