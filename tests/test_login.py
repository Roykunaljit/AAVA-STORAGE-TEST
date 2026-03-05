import pytest
import logging
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage


logger = logging.getLogger(__name__)


class TestLogin:
    """Login page test cases."""

    @pytest.mark.smoke
    @pytest.mark.login
    def test_valid_login(
        self, clean_browser, base_url, admin_credentials
    ):
        """TC-001: Verify successful login with valid credentials."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        assert login_page.is_login_page_loaded()
        login_page.login(
            admin_credentials["username"],
            admin_credentials["password"]
        )
        dashboard = DashboardPage(clean_browser)
        assert dashboard.is_dashboard_loaded()
        assert "dashboard" in clean_browser.current_url

    @pytest.mark.smoke
    @pytest.mark.login
    def test_invalid_login(
        self, clean_browser, base_url, invalid_credentials
    ):
        """TC-002: Verify error message with invalid credentials."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        login_page.login(
            invalid_credentials["username"],
            invalid_credentials["password"]
        )
        assert login_page.is_error_displayed()
        error = login_page.get_error_message()
        assert "Invalid" in error

    @pytest.mark.login
    def test_empty_username(
        self, clean_browser, base_url
    ):
        """TC-003: Verify error when username is empty."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        login_page.login("", "somepassword")
        assert login_page.is_error_displayed()

    @pytest.mark.login
    def test_empty_password(
        self, clean_browser, base_url
    ):
        """TC-004: Verify error when password is empty."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        login_page.login("user@example.com", "")
        assert login_page.is_error_displayed()

    @pytest.mark.login
    def test_remember_me(
        self, clean_browser, base_url, admin_credentials
    ):
        """TC-005: Verify remember me functionality."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        login_page.check_remember_me()
        login_page.login(
            admin_credentials["username"],
            admin_credentials["password"]
        )
        dashboard = DashboardPage(clean_browser)
        assert dashboard.is_dashboard_loaded()

    @pytest.mark.login
    def test_forgot_password_link(
        self, clean_browser, base_url
    ):
        """TC-006: Verify forgot password link works."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        login_page.click_forgot_password()
        assert "forgot" in clean_browser.current_url.lower()

    @pytest.mark.login
    def test_signup_link(
        self, clean_browser, base_url
    ):
        """TC-007: Verify sign up link navigation."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        login_page.click_signup()
        assert "signup" in clean_browser.current_url.lower()

    @pytest.mark.regression
    @pytest.mark.login
    def test_login_page_elements(
        self, clean_browser, base_url
    ):
        """TC-008: Verify all login page elements are present."""
        login_page = LoginPage(clean_browser)
        login_page.navigate_to_login(base_url)
        assert login_page.is_login_page_loaded()
        assert login_page.is_element_visible(
            login_page.locators.LOGO_IMAGE
        )
        assert login_page.is_element_visible(
            login_page.locators.FORGOT_PASSWORD_LINK
        )