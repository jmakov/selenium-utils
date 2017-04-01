# A toolbox for advanced Selenium acrobatics

## Compatibility
Because of type hinting is extensively used, only Python 3.5 and above are supported.

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
alert.handle_alert(driver, accept_alert=True)

# let's say we opened multiple windows and tabs and want to close all but the current one
tab.close_all_tabs_except_given(driver, driver.current_window_handle)

# If an element is moving there's a high probability the clicks will miss the element.
# E.g. if a menu is expanding, we can wait until the animation stops.
element.wait_until_stops_moving(button_send)
button_send.click()
```