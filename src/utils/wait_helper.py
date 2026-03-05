import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


logger = logging.getLogger(__name__)


class WaitHelper:
    """Custom wait utilities."""

    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=15):
        """Wait until element is visible."""
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            logger.error(
                f"Element not visible after {timeout}s: {locator}"
            )
            raise

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=15):
        """Wait until element is clickable."""
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            logger.error(
                f"Element not clickable after {timeout}s: {locator}"
            )
            raise

    @staticmethod
    def wait_for_element_invisible(driver, locator, timeout=15):
        """Wait until element disappears."""
        try:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_for_text_in_element(
        driver, locator, text, timeout=15
    ):
        """Wait for specific text in element."""
        try:
            WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element(
                    locator, text
                )
            )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_for_url_contains(driver, partial_url, timeout=15):
        """Wait for URL to contain text."""
        try:
            WebDriverWait(driver, timeout).until(
                EC.url_contains(partial_url)
            )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_for_page_ready(driver, timeout=30):
        """Wait for page to be fully loaded."""
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    @staticmethod
    def hard_wait(seconds):
        """Explicit sleep — use sparingly."""
        logger.warning(f"Hard wait: {seconds}s")
        time.sleep(seconds)

    @staticmethod
    def wait_for_ajax(driver, timeout=15):
        """Wait for all AJAX calls to complete."""
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script(
                    "return jQuery.active == 0"
                )
            )
        except Exception:
            logger.warning("jQuery not found or AJAX wait failed")

    @staticmethod
    def wait_for_staleness(driver, element, timeout=10):
        """Wait for element to become stale (removed from DOM)."""
        try:
            WebDriverWait(driver, timeout).until(
                EC.staleness_of(element)
            )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_for_new_window(driver, current_handles, timeout=10):
        """Wait for a new window/tab to open."""
        WebDriverWait(driver, timeout).until(
            lambda d: len(d.window_handles) > len(current_handles)
        )