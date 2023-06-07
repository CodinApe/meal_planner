from django import forms

from bootstrap_datepicker_plus.widgets import DatePickerInput

from.models import Plan

class NewPlan(forms.ModelForm):
    class meta:
        model = Plan
        fields = ['date', 'breakfast']
        widgets = {'date': DatePickerInput()}