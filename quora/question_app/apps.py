from django.apps import AppConfig


class QuestionAppConfig(AppConfig):
    """Configuration class of question_app.
    It is also responsible to add default id(pk) in database tables.

    Args:
        AppConfig (class): Django inbuilt app configuration
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "question_app"
