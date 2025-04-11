from django import forms

from .models import Answer, Question


class QuestionForm(forms.ModelForm):
    """Question form to create new questions

    Args:
        forms.ModelForm (class): Inbuilt django class to generate form using model
    """

    class Meta:
        """
        Meta class to define configs of form
        """

        model = Question
        fields = ["question", "description"]

        widget = {
            "question": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class AnswerForm(forms.ModelForm):
    """Answer form to create new answers

    Args:
        forms.ModelForm (class): Inbuilt django class to generate form using model
    """

    class Meta:
        """
        Meta class to define configs of form
        """

        model = Answer
        fields = ["answer"]
