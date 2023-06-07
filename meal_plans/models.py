from django.db import models

# Create your models here.

class Plan(models.Model):
    """create a plan for a certain day"""
    date = models.DateField()
    breakfast = models.TextField(default="")
    lunch = models.TextField(default="")
    dinner = models.TextField(default="")
    snacks = models.TextField(default="")

    def __str__(self):
        return str(self.date)
