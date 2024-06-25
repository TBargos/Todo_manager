from django.db import models

class Task(models.Model):
    taskname = models.CharField(max_length=80)
    status = models.BooleanField(default=True)
