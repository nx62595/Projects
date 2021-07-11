from django.db import models

# Create your models here.
class Questions(models.Model):
    Gymworkout = models.CharField(max_length=100)
    started_when = models.DateTimeField

    def __str__(self):
        return self.Gymworkout

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 100)
    current_weight = models.IntegerField()
    days = models.IntegerField(default=0)

    def __int__(self):
        return self.current_weight