from django.shortcuts import render

from .models import Plan

# Create your views here.

def index(request):
    """Home apge for meal planner]"""
    return render(request, 'meal_plans/index.html')

def plans(request):
    """Show all the plans"""
    plans = Plan.objects.order_by('date')
    context = {'plans': plans}
    return render(request, 'meal_plans/plans.html', context)

def plan(request, plan_id):
    """Shows page of specific plan for selected day"""
    plan = Plan.objects.get(id=plan_id)
    
    context = {'plan': plan}
    return render(request, 'meal_plans/plan.html', context)

    
