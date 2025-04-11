from django.db import models


class CommonFields(models.Model):
    """Abstract class to declare common functionality

    Args:
        models.Model (class): django inbuilt model class
    """

    user = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class to declare abstraction"""

        abstract = True


class Question(CommonFields):
    """Class to declare questions table schema

    Args:
        CommonFields (class): Abstraction model
    """

    question = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Magic method to define string representation"""
        return self.question


class Answer(CommonFields):
    """Class to declare answers table schema

    Args:
        CommonFields (class): Abstraction model
    """

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    likes = models.CharField(max_length=200)

    def __str__(self):
        """Magic method to define string representation"""
        return self.answer
