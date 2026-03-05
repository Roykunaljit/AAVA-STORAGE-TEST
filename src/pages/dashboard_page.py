import logging
from src.base.base_page import BasePage
from src.locators.dashboard_locators import DashboardLocators


logger = logging.getLogger(__name__)


class DashboardPage(BasePage):
    """Page object for the Dashboard page."""

    URL = "/dashboard"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators

    def is_dashboard_loaded(self):
        """Verify dashboard page is loaded."""
        return self.is_element_visible(
            self.locators.WELCOME_BANNER
        )

    def get_welcome_text(self):
        """Get welcome banner text."""
        return self.get_text(
            self.locators.WELCOME_BANNER
        )

    def click_logout(self):
        """Click logout button."""
        self.click(self.locators.LOGOUT_BUTTON)
        logger.info("Clicked logout")

    def get_notification_count(self):
        """Get notification count."""
        text = self.get_text(
            self.locators.NOTIFICATION_COUNT
        )
        return int(text) if text.isdigit() else 0

    def click_notification_bell(self):
        """Click notification bell."""
        self.click(
            self.locators.NOTIFICATION_BELL
        )

    def search_global(self, query):
        """Perform global search."""
        self.type_text(
            self.locators.SEARCH_INPUT, query
        )
        self.click(self.locators.SEARCH_BUTTON)

    def get_total_stats(self):
        """Get total stats card value."""
        return self.get_text(
            self.locators.STATS_CARD_TOTAL
        )

    def get_active_stats(self):
        """Get active stats card value."""
        return self.get_text(
            self.locators.STATS_CARD_ACTIVE
        )

    def click_settings(self):
        """Navigate to settings."""
        self.click(self.locators.SETTINGS_LINK)

    def click_profile(self):
        """Navigate to profile."""
        self.click(self.locators.PROFILE_LINK)

    def is_sidebar_visible(self):
        """Check if sidebar is visible."""
        return self.is_element_visible(
            self.locators.SIDEBAR_MENU
        )

    def get_recent_activity_rows(self):
        """Get recent activity table rows."""
        table = self.find_element(
            self.locators.RECENT_ACTIVITY_TABLE
        )
        rows = table.find_elements_by_tag_name("tr")
        return len(rows) - 1  # minus header

    def get_footer_text(self):
        """Get footer text."""
        return self.get_text(
            self.locators.FOOTER_TEXT
        )