from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging


logger = logging.getLogger(__name__)


class BasePage:
    """Base page object that all page objects inherit from."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        """Find a single element with explicit wait."""
        logger.info(f"Finding element: {locator}")
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        """Find multiple elements."""
        logger.info(f"Finding elements: {locator}")
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        """Click on an element."""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        logger.info(f"Clicking: {locator}")
        element.click()

    def type_text(self, locator, text):
        """Clear field and type text."""
        element = self.find_element(locator)
        element.clear()
        logger.info(f"Typing into: {locator}")
        element.send_keys(text)

    def get_text(self, locator):
        """Get text of an element."""
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def is_element_present(self, locator, timeout=5):
        """Check if element is present in DOM."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def wait_for_page_load(self):
        """Wait for page to fully load."""
        self.wait.until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def scroll_to_element(self, locator):
        """Scroll to make element visible."""
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

    def take_screenshot(self, filename):
        """Take a screenshot."""
        self.driver.save_screenshot(f"screenshots/{filename}.png")
        logger.info(f"Screenshot saved: {filename}")

    def get_current_url(self):
        """Get current page URL."""
        return self.driver.current_url

    def get_page_title(self):
        """Get current page title."""
        return self.driver.title

    def switch_to_frame(self, locator):
        """Switch to iframe."""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        """Switch back to default content."""
        self.driver.switch_to.default_content()

    def accept_alert(self):
        """Accept browser alert."""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def dismiss_alert(self):
        """Dismiss browser alert."""
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

    def select_dropdown_by_text(self, locator, text):
        """Select dropdown option by visible text."""
        from selenium.webdriver.support.ui import Select
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def hover_over(self, locator):
        """Hover over an element."""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()