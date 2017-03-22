from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def close_all_tabs_except_given(driver: WebDriver, window_handle: str):
    """
    Closes all tabs except the given window handle which can be obtained by driver.current_window_handle
    """
    for handle in driver.window_handles:
        if handle != window_handle:
            driver.switch_to.window(handle)
            driver.close()

    driver.switch_to.window(window_handle)


def wait_until_all_tabs_loaded(driver: WebDriver):
    """
    When multiple windows are loading in the background, we wait until all are done
    """
    original_window_handle = driver.current_window_handle

    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.find_element(By.CSS_SELECTOR, "html")

    driver.switch_to.window(original_window_handle)


def close_all_except_containing_urls(driver: WebDriver, urls: list):
    current_window_handle = driver.current_window_handle

    for handle in driver.window_handles:
        if handle != current_window_handle:
            driver.switch_to.window(handle)
            window_url = driver.current_url

            if not any([url in window_url for url in urls]):
                driver.close()
