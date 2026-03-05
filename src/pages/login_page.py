import logging
from src.base.base_page import BasePage
from src.locators.login_locators import LoginLocators


logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Page object for the Login page."""

    URL = "/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators

    def navigate_to_login(self, base_url):
        """Navigate to the login page."""
        self.driver.get(f"{base_url}{self.URL}")
        self.wait_for_page_load()
        logger.info("Navigated to login page")

    def enter_username(self, username):
        """Enter username."""
        self.type_text(
            self.locators.USERNAME_INPUT, username
        )

    def enter_password(self, password):
        """Enter password."""
        self.type_text(
            self.locators.PASSWORD_INPUT, password
        )

    def click_login(self):
        """Click the login button."""
        self.click(self.locators.LOGIN_BUTTON)

    def login(self, username, password):
        """Perform complete login."""
        logger.info(f"Logging in as: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Get login error message text."""
        return self.get_text(
            self.locators.ERROR_MESSAGE
        )

    def is_error_displayed(self):
        """Check if error message is visible."""
        return self.is_element_visible(
            self.locators.ERROR_MESSAGE
        )

    def click_forgot_password(self):
        """Click forgot password link."""
        self.click(
            self.locators.FORGOT_PASSWORD_LINK
        )

    def click_signup(self):
        """Click sign up link."""
        self.click(self.locators.SIGNUP_LINK)

    def check_remember_me(self):
        """Check the remember me checkbox."""
        self.click(
            self.locators.REMEMBER_ME_CHECKBOX
        )

    def is_login_page_loaded(self):
        """Verify login page is loaded."""
        return (
            self.is_element_visible(
                self.locators.USERNAME_INPUT
            )
            and self.is_element_visible(
                self.locators.LOGIN_BUTTON
            )
        )

    def login_with_google_sso(self):
        """Click Google SSO button."""
        self.click(
            self.locators.SSO_GOOGLE_BUTTON
        )

    def enter_two_fa_code(self, code):
        """Enter 2FA code."""
        self.type_text(
            self.locators.TWO_FA_INPUT, code
        )
        self.click(self.locators.TWO_FA_SUBMIT)