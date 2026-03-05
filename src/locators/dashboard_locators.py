from selenium.webdriver.common.by import By


class DashboardLocators:
    """Locators for the Dashboard page."""

    WELCOME_BANNER = (By.CSS_SELECTOR, ".welcome-banner")
    USER_AVATAR = (By.CSS_SELECTOR, ".user-avatar")
    LOGOUT_BUTTON = (By.ID, "logout-btn")
    SIDEBAR_MENU = (By.CSS_SELECTOR, ".sidebar-menu")
    NOTIFICATION_BELL = (By.ID, "notification-bell")
    NOTIFICATION_COUNT = (By.CSS_SELECTOR, ".notification-count")
    SEARCH_INPUT = (By.ID, "global-search")
    SEARCH_BUTTON = (By.ID, "search-btn")
    STATS_CARD_TOTAL = (By.CSS_SELECTOR, ".stats-card.total")
    STATS_CARD_ACTIVE = (By.CSS_SELECTOR, ".stats-card.active")
    STATS_CARD_PENDING = (By.CSS_SELECTOR, ".stats-card.pending")
    RECENT_ACTIVITY_TABLE = (By.CSS_SELECTOR, "table.recent-activity")
    QUICK_ACTIONS_MENU = (By.CSS_SELECTOR, ".quick-actions")
    SETTINGS_LINK = (By.LINK_TEXT, "Settings")
    PROFILE_LINK = (By.LINK_TEXT, "Profile")
    HELP_LINK = (By.LINK_TEXT, "Help")
    FOOTER_TEXT = (By.CSS_SELECTOR, ".footer-text")