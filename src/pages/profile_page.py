import logging
from selenium.webdriver.common.by import By
from src.base.base_page import BasePage


logger = logging.getLogger(__name__)


class ProfileLocators:
    """Locators for Profile page."""
    PROFILE_NAME = (By.ID, "profile-name")
    PROFILE_EMAIL = (By.ID, "profile-email")
    EDIT_BUTTON = (By.ID, "edit-profile-btn")
    SAVE_BUTTON = (By.ID, "save-profile-btn")
    CANCEL_BUTTON = (By.ID, "cancel-edit-btn")
    AVATAR_UPLOAD = (By.ID, "avatar-upload")
    NAME_INPUT = (By.ID, "name-input")
    EMAIL_INPUT = (By.ID, "email-input")
    PHONE_INPUT = (By.ID, "phone-input")
    BIO_TEXTAREA = (By.ID, "bio-textarea")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".toast-success")
    ERROR_TOAST = (By.CSS_SELECTOR, ".toast-error")
    CHANGE_PASSWORD_LINK = (By.LINK_TEXT, "Change Password")
    DELETE_ACCOUNT_BUTTON = (By.ID, "delete-account-btn")
    CONFIRM_DELETE_BUTTON = (By.ID, "confirm-delete-btn")


class ProfilePage(BasePage):
    """Page object for the Profile page."""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfileLocators

    def get_profile_name(self):
        """Get displayed profile name."""
        return self.get_text(
            self.locators.PROFILE_NAME
        )

    def get_profile_email(self):
        """Get displayed profile email."""
        return self.get_text(
            self.locators.PROFILE_EMAIL
        )

    def click_edit(self):
        """Click edit profile button."""
        self.click(self.locators.EDIT_BUTTON)

    def update_name(self, name):
        """Update profile name."""
        self.type_text(
            self.locators.NAME_INPUT, name
        )

    def update_email(self, email):
        """Update profile email."""
        self.type_text(
            self.locators.EMAIL_INPUT, email
        )

    def update_phone(self, phone):
        """Update phone number."""
        self.type_text(
            self.locators.PHONE_INPUT, phone
        )

    def update_bio(self, bio):
        """Update bio text."""
        self.type_text(
            self.locators.BIO_TEXTAREA, bio
        )

    def save_profile(self):
        """Save profile changes."""
        self.click(self.locators.SAVE_BUTTON)

    def cancel_edit(self):
        """Cancel editing."""
        self.click(self.locators.CANCEL_BUTTON)

    def is_success_shown(self):
        """Check if success toast is shown."""
        return self.is_element_visible(
            self.locators.SUCCESS_TOAST
        )

    def click_change_password(self):
        """Click change password link."""
        self.click(
            self.locators.CHANGE_PASSWORD_LINK
        )

    def delete_account(self):
        """Delete account flow."""
        self.click(
            self.locators.DELETE_ACCOUNT_BUTTON
        )
        self.click(
            self.locators.CONFIRM_DELETE_BUTTON
        )