from django.db import models

# Create your models here.
class Goal(models.Model):
    name = models.CharField(default="New Goal", max_length=50)
    reason = models.TextField(default="", max_length=500)
    completion_percentage = models.DecimalField(decimal_places=2, max_digits=5 ,default=0)

class Note(models.Model):
    text = models.TextField(default="you added a note with no value")
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    