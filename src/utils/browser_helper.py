import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


logger = logging.getLogger(__name__)


class BrowserHelper:
    """Helper class for browser management."""

    @staticmethod
    def create_chrome_driver(headless=False):
        """Create Chrome WebDriver instance."""
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        logger.info("Chrome driver created")
        return driver

    @staticmethod
    def create_firefox_driver(headless=False):
        """Create Firefox WebDriver instance."""
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(10)
        logger.info("Firefox driver created")
        return driver

    @staticmethod
    def quit_driver(driver):
        """Safely quit the driver."""
        if driver:
            try:
                driver.quit()
                logger.info("Driver quit successfully")
            except Exception as e:
                logger.error(f"Error quitting driver: {e}")

    @staticmethod
    def clear_cookies(driver):
        """Clear all cookies."""
        driver.delete_all_cookies()
        logger.info("Cookies cleared")

    @staticmethod
    def get_browser_logs(driver):
        """Get browser console logs."""
        try:
            return driver.get_log("browser")
        except Exception:
            return []

    @staticmethod
    def set_window_size(driver, width, height):
        """Set browser window size."""
        driver.set_window_size(width, height)

    @staticmethod
    def maximize_window(driver):
        """Maximize browser window."""
        driver.maximize_window()

    @staticmethod
    def refresh_page(driver):
        """Refresh current page."""
        driver.refresh()

    @staticmethod
    def go_back(driver):
        """Navigate back."""
        driver.back()

    @staticmethod
    def go_forward(driver):
        """Navigate forward."""
        driver.forward()

    @staticmethod
    def execute_js(driver, script, *args):
        """Execute JavaScript."""
        return driver.execute_script(script, *args)

    @staticmethod
    def switch_to_new_window(driver):
        """Switch to newly opened window."""
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

    @staticmethod
    def close_current_window(driver):
        """Close current window and switch back."""
        driver.close()
        handles = driver.window_handles
        if handles:
            driver.switch_to.window(handles[0])