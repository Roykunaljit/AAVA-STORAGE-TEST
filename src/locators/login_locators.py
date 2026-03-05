from selenium.webdriver.common.by import By


class LoginLocators:
    """Locators for the Login page."""

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")
    LOADING_SPINNER = (By.CSS_SELECTOR, ".spinner")
    LOGO_IMAGE = (By.CSS_SELECTOR, "img.logo")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    SSO_GOOGLE_BUTTON = (By.ID, "sso-google")
    SSO_GITHUB_BUTTON = (By.ID, "sso-github")
    CAPTCHA_FRAME = (By.CSS_SELECTOR, "iframe.captcha-frame")
    TWO_FA_INPUT = (By.ID, "two-fa-code")
    TWO_FA_SUBMIT = (By.ID, "two-fa-submit")