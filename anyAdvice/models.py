from django.db import models
from django.utils import timezone


# Create your models here.
class AdviceModel(models.Model):
    advice = models.CharField(max_length=100)
    slip_id = models.IntegerField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.advice
