# Common utility functions for dealing with Selenium Webdriver

## Compatibility
Because of type hinting is extensively used, only Python 3.5 and above is supported.

## Examples
```python
from selenium import webdriver

from selenium_utils import element
from selenium_utils import screenshot
from selenium_utils import alert
from selenium_utils import tab



driver = webdriver.Chrome()

# find element and scroll it into view
page_header_pixels = 200
button_send = driver.find_element_by_css_selector("#button_send")
element.scroll_into_view(driver, button_send, page_header_pixels)
button_send.click()

# make screenshot of the whole website
screenshot.resize_to_page_size(driver)
screenshot.get_screenshot(driver, "screenshot.png")

# handle expected alert
alert.wait_until_alert_is_present(driver)
alert.accept_alert(driver, accept_alert=True)

# let's say we opened multiple windows and tabs and want to close all but the current one
tab.close_all_tabs_except_given(driver, driver.current_window_handle)
```