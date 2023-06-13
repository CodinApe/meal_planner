from django import forms

from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Plan

class NewPlan(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['date', 'breakfast', 'lunch', 'dinner', 'snacks']
        widgets = {'date': DatePickerInput()}