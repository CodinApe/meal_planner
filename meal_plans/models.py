from typing import Iterable, Optional
from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import datetime

# Create your models here.

class Plan(models.Model):
    """create a plan for a certain day"""
    date = models.DateField()
    # goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

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

    def return_cals(self):
        cals = 0
        for item in self.fooditem_set.all():
            if item.calories != None:
                cals += item.calories
        return cals
    
    def return_fat(self):
        fat = 0
        for item in self.fooditem_set.all():
            if item.fat != None:
                fat += item.fat
        return fat
    
    def return_protein(self):
        protein = 0
        for item in self.fooditem_set.all():
            if item.protein != None:
                protein+= item.protein 
        return protein
    
    def return_carbs(self):
        carbs = 0
        for item in self.fooditem_set.all():
            if item.carbohydrates != None:
                carbs += item.carbohydrates
        return carbs

    def __str__(self):
        return str(self.date.strftime("%B %d %Y"))

class FoodItem(models.Model):
    """create foo item with fat, protein, and carb content"""
    item = models.TextField(blank=True)
    calories = models.PositiveIntegerField(null=True, blank=True)
    fat = models.PositiveIntegerField(null=True, blank=True)
    protein = models.PositiveIntegerField(null=True, blank=True)
    carbohydrates = models.PositiveIntegerField(null=True, blank=True) 

    plan = models.ManyToManyField(Plan)

    def __str__(self):
        return self.item    
    
class Goal(models.Model):
    """The goal the user creates to track their goals in meal planning/prep"""
    name = "Goal"
    calories = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    carbs = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    # Delete once users is set up and implement - user= models.OneToOneField(User, models.on_delete=CASCADE)
    def save(self, *args, **kwargs):
        if Goal.objects.exists():
            # If a goal exists, update its attributes
            existing_goal = Goal.objects.first()
            existing_goal.calories = self.calories
            existing_goal.fat = self.fat
            existing_goal.protein = self.protein
            existing_goal.carbs = self.carbs
            Goal.objects.filter(pk=existing_goal.pk).update(
                calories=self.calories,
                fat=self.fat,
                protein=self.protein,
                carbs=self.carbs
            )
        else:
            # saves goal if none exists already
            super(Goal, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # prevents deletion
        pass   
