from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    def __str__(self):
        return f'제목: {self.question_text} 날짜:{self.pub_date}' #self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    #on_delete: Question이 삭제되면 관련된 Choice도 삭제되도록 설정
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__ (self):
        return f'{self.choice_text}'