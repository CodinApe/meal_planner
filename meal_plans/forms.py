from django import forms
from django.forms import formset_factory

# from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Plan, FoodItem


class NewFoodItem(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['item', 'fat', 'carbohydrates', 'protein']
        widgets = {
            'item' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class NewPlan(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['date']
        # Sets a widget with class of datepicker to utilize jquery datepicker 
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        # {'date': DatePickerInput()}

# Form to take a user input food item to scan the sqlite database and api call in views.py
class SearchFoods(forms.Form):
    foodItem = forms.CharField(label="Search food items", max_length=80)
        

        