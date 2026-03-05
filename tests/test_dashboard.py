import pytest
import logging
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage


logger = logging.getLogger(__name__)


class TestDashboard:
    """Dashboard page test cases."""

    def _login_first(
        self, browser, base_url, credentials
    ):
        """Helper: Login before dashboard tests."""
        login_page = LoginPage(browser)
        login_page.navigate_to_login(base_url)
        login_page.login(
            credentials["username"],
            credentials["password"]
        )

    @pytest.mark.smoke
    @pytest.mark.dashboard
    def test_dashboard_loads(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-009: Verify dashboard loads after login."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        assert dashboard.is_dashboard_loaded()

    @pytest.mark.dashboard
    def test_welcome_message(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-010: Verify welcome message shows username."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        welcome = dashboard.get_welcome_text()
        assert "Welcome" in welcome

    @pytest.mark.dashboard
    def test_logout(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-011: Verify logout works."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        dashboard.click_logout()
        assert "login" in clean_browser.current_url.lower()

    @pytest.mark.dashboard
    def test_sidebar_visible(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-012: Verify sidebar is visible."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        assert dashboard.is_sidebar_visible()

    @pytest.mark.dashboard
    def test_global_search(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-013: Verify global search works."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        dashboard.search_global("test query")

    @pytest.mark.dashboard
    def test_notification_bell(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-014: Verify notification bell is clickable."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        dashboard.click_notification_bell()

    @pytest.mark.regression
    @pytest.mark.dashboard
    def test_stats_cards_visible(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-015: Verify stats cards are displayed."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        total = dashboard.get_total_stats()
        assert total is not None

    @pytest.mark.dashboard
    def test_navigate_to_settings(
        self, clean_browser, base_url,
        admin_credentials
    ):
        """TC-016: Verify settings navigation."""
        self._login_first(
            clean_browser, base_url,
            admin_credentials
        )
        dashboard = DashboardPage(clean_browser)
        dashboard.click_settings()
        assert "settings" in clean_browser.current_url.lower()