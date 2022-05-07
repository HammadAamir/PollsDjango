from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime
# Create your models here.
class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')
    
    
    @admin.display(
        boolean = True,
        ordering = 'pubDate',
        description = 'Published Recently?',
    )
    def wasPublishedRecently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pubDate <= now
    
    def __str__(self):
        return self.questionText
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choiceText