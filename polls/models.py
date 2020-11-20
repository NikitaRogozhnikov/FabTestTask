from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class Question(models.Model):
    TEXT='text'
    RADIO='radio'
    CHECK='check'
    CHOICES=[(TEXT,'t'),(RADIO,'r'),(CHECK,'c')] 
    title = models.CharField(max_length=4096)
    end_date = models.DateTimeField(default=datetime.today()+ timedelta(days=1))
    ques_type=models.CharField(max_length=5,choices=CHOICES,default='t')
    
    def __str__(self):
           return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=4096)
    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)    
    created = models.DateTimeField(auto_now_add=True)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING,blank=True)
    def __str__(self):
        return self.choice.title