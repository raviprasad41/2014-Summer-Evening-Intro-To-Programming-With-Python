from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=4096)
    description = models.TextField()
    from_date_time = models.DateTimeField()
    to_date_time = models.DateTimeField()

    def __str__(self):
        return self.title


class KeyWord(models.Model):
    word = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.word