from django.db import models
from django.contrib.auth.models import User

# Create your models here.
statusChoice = [
    ("Complete", "Complete"),
    ("Pending", "Pending"),
]

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    duedate = models.DateTimeField()
    status = models.CharField(max_length=52,choices=statusChoice, default="Pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    