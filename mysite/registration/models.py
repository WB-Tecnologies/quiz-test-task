from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=100,default="")
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    option5 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    quiz = models.ForeignKey(Quiz)

    def __str__(self):
        return self.question
