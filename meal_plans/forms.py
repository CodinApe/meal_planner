from django import forms

from.models import Plan

class NewPlan(forms.ModelForm):
    class meta:
        model = Plan
        fields = ['date', 'breakfast']