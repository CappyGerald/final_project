from django import forms
from .models import Question, Choice

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = question.choices.all()
            choice_list = [(choice.id, choice.choice_text) for choice in choices]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(
                label=question.text,
                choices=choice_list,
                widget=forms.RadioSelect
            )


