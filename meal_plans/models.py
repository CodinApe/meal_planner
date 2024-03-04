from typing import Iterable, Optional
from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

class Plan(models.Model):
    """create a plan for a certain day"""
    date = models.DateField()
    """breakfast = models.TextField(default="") # original functionality before adding FoodItem class.
    lunch = models.TextField(default="")
    dinner = models.TextField(default="")
    snacks = models.TextField(default="")"""

    # current_date = datetime.date.today()
    # the_day = current_date.weekday()
    # week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # current_day = week_days[the_day]

    # allows user to delete item based on boolean
    # delete_plan = False

    def clean(self): 
        """Performs validation to data and inputs automatically, but this adds a 
        new validation for when a date is already used for a plan."""
        previous_date = Plan.objects.filter(date = self.date) 
        previous_date.exclude(pk=self.pk)
        if previous_date.exists():
            raise ValidationError("You have a plan for this day already. Try updating your plan.")
    
    def save(self):
        self.clean()
        super().save()

    @property
    def day_of_week(self):
        return self.date.strftime('%A')

    def __str__(self):
        return str(self.date.strftime("%B %d %Y"))

class FoodItem(models.Model):
    """create foo item with fat, protein, and carb content"""
    item = models.TextField(blank=True)
    fat = models.PositiveIntegerField(null=True, blank=True)
    protein = models.PositiveIntegerField(null=True, blank=True)
    carbohydrates = models.PositiveIntegerField(null=True, blank=True) 

    plan = models.ManyToManyField(Plan)

    def __str__(self):
        return self.item    
    
    

    
    



    

    
