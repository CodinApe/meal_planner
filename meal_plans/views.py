from django.shortcuts import render, redirect

from .models import Plan

from .forms import NewPlan

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

def new_plan(request):
    """Add a new plan for acertain day"""
    if request != 'POST':
        # no data submitted; create blank form
        form = NewPlan()
    else:
        # POST data submitted; process the data.
        form = NewPlan(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_plams:index')
    context = {'form': form}
    return render(request, 'meal_plans/new_plan.html', context)

    
