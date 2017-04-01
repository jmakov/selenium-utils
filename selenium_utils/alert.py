import logging

from selenium.common import exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


def wait_until_alert_is_present(driver: WebDriver, wait_seconds=1):
    """
    Waits until an alert is present

    Returns:
        selenium.webdriver.common.alert.Alert
    """
    return WebDriverWait(
        driver,
        wait_seconds) \
        .until(EC.alert_is_present())


def handle_alert(driver: WebDriver, accept_alert: bool) -> bool:
    """
    Accepts alert if present.
    """
    try:
        alert = driver.switch_to.alert

        if accept_alert:
            alert.accept()
        else:
            alert.dismiss()

        return True
    except exceptions.NoAlertPresentException as e:
        return False
