"""
auth_app's configuration file.
"""

from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    """Configuration class of auth_app.
    It is also responsible to add default id(pk) in database tables.

    Args:
        AppConfig (class): Django inbuilt app configuration
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "auth_app"
