from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
