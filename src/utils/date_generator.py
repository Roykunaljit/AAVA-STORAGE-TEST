import random
import string
import uuid
from datetime import datetime, timedelta


class DataGenerator:
    """Generates random test data."""

    @staticmethod
    def random_email():
        """Generate random email."""
        name = ''.join(
            random.choices(string.ascii_lowercase, k=8)
        )
        domain = random.choice([
            "test.com", "example.com",
            "demo.org", "mail.test"
        ])
        return f"{name}@{domain}"

    @staticmethod
    def random_username(length=10):
        """Generate random username."""
        return ''.join(
            random.choices(
                string.ascii_lowercase + string.digits,
                k=length
            )
        )

    @staticmethod
    def random_password(length=12):
        """Generate random password."""
        chars = (
            string.ascii_letters
            + string.digits
            + "!@#$%"
        )
        return ''.join(
            random.choices(chars, k=length)
        )

    @staticmethod
    def random_phone():
        """Generate random phone number."""
        return f"+1{''.join(random.choices(string.digits, k=10))}"

    @staticmethod
    def random_name():
        """Generate random full name."""
        first_names = [
            "Alice", "Bob", "Charlie",
            "Diana", "Eve", "Frank"
        ]
        last_names = [
            "Smith", "Jones", "Brown",
            "Wilson", "Taylor", "Davis"
        ]
        return (
            f"{random.choice(first_names)} "
            f"{random.choice(last_names)}"
        )

    @staticmethod
    def random_string(length=10):
        """Generate random alphanumeric string."""
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=length
            )
        )

    @staticmethod
    def random_uuid():
        """Generate UUID."""
        return str(uuid.uuid4())

    @staticmethod
    def random_date(days_range=365):
        """Generate random date within range."""
        base = datetime.now()
        offset = random.randint(0, days_range)
        return (base - timedelta(days=offset)).strftime(
            "%Y-%m-%d"
        )

    @staticmethod
    def random_integer(min_val=1, max_val=1000):
        """Generate random integer."""
        return random.randint(min_val, max_val)

    @staticmethod
    def random_boolean():
        """Generate random boolean."""
        return random.choice([True, False])

    @staticmethod
    def random_address():
        """Generate random address."""
        number = random.randint(1, 9999)
        streets = [
            "Main St", "Oak Ave",
            "Elm Blvd", "Park Dr"
        ]
        cities = [
            "Springfield", "Portland",
            "Austin", "Denver"
        ]
        return (
            f"{number} {random.choice(streets)}, "
            f"{random.choice(cities)}"
        )