from django.db import models
import datetime

# Create your models here.

class Plan(models.Model):
    """create a plan for a certain day"""
    date = models.DateField()
    #current = str(date)
    #dayofweek = date(current).strftime('%A')
    #current = datetime().date()
    #dayofweek = current.strftime('%A')
    breakfast = models.TextField(default="")
    lunch = models.TextField(default="")
    dinner = models.TextField(default="")
    snacks = models.TextField(default="")

    @property
    def day_of_week(self):
        return self.date.strftime('%A')

    def __str__(self):
        return str(self.date)
    
    
    

    
    



    

    
