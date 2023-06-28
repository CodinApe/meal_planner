from django import forms
from django.forms import formset_factory

from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Plan, FoodItem


class NewFoodItem(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['item', 'fat', 'carbohydrates', 'protein']

class NewPlan(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['date']
        widgets = {'date': DatePickerInput()}
        

        