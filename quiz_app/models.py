from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    topic = models.ForeignKey(Topic, related_name = 'questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

def __str__(self):
    return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices' , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    
class UserQuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_attempted = models.DateTimeField(auto_now_add=True)
