from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = question.choice.all()
            choice_list = [(choice.id, choice.choice.text) for choice in quesion.choices.all()]
            self.fields[f"quesion_{question.id}"] = forms.ChoiceField(
                label=question.text,
                choices = choice_list,
                widget=forms.RadioSelect
            )

