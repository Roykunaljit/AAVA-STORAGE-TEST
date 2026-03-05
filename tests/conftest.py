import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


logger = logging.getLogger(__name__)


BASE_URL = "https://staging.example.com"


@pytest.fixture(scope="session")
def browser():
    """Session-scoped browser fixture."""
    logger.info("Creating session browser...")
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    logger.info("Closing session browser...")
    driver.quit()


@pytest.fixture(scope="function")
def clean_browser(browser):
    """Clear state before each test."""
    browser.delete_all_cookies()
    yield browser


@pytest.fixture
def base_url():
    """Return base URL."""
    return BASE_URL


@pytest.fixture
def admin_credentials():
    """Return admin credentials."""
    return {
        "username": "admin@example.com",
        "password": "admin123"
    }


@pytest.fixture
def standard_credentials():
    """Return standard user credentials."""
    return {
        "username": "user@example.com",
        "password": "user123"
    }


@pytest.fixture
def invalid_credentials():
    """Return invalid credentials."""
    return {
        "username": "invalid@example.com",
        "password": "wrong_password"
    }


def pytest_configure(config):
    """Configure custom markers."""
    config.addinivalue_line(
        "markers", "smoke: Smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: Regression tests"
    )
    config.addinivalue_line(
        "markers", "login: Login tests"
    )
    config.addinivalue_line(
        "markers", "dashboard: Dashboard tests"
    )