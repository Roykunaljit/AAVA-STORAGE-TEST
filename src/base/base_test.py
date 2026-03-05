import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


logger = logging.getLogger(__name__)


class BaseTest:
    """Base test class with setup and teardown."""

    driver = None

    @classmethod
    def setup_class(cls):
        """Setup browser before all tests in class."""
        logger.info("Setting up browser...")
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        logger.info("Browser setup complete")

    @classmethod
    def teardown_class(cls):
        """Cleanup after all tests in class."""
        if cls.driver:
            logger.info("Closing browser...")
            cls.driver.quit()

    def setup_method(self):
        """Run before each test method."""
        logger.info(f"Starting test: {self.__class__.__name__}")

    def teardown_method(self):
        """Run after each test method."""
        logger.info(f"Finished test: {self.__class__.__name__}")

    def navigate_to(self, url):
        """Navigate to a URL."""
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def assert_page_title(self, expected_title):
        """Assert page title matches."""
        actual = self.driver.title
        assert actual == expected_title, (
            f"Expected title '{expected_title}', got '{actual}'"
        )

    def assert_url_contains(self, partial_url):
        """Assert current URL contains text."""
        current = self.driver.current_url
        assert partial_url in current, (
            f"Expected URL to contain '{partial_url}', got '{current}'"
        )