from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
import calendar
import datetime

from .models import Plan, FoodItem

from .forms import NewPlan, NewFoodItem

# Create your views here.

def index(request):
    """Home page for meal planner"""
    return render(request, 'meal_plans/index.html')

def plans(request):
    """Show all the plans"""
    plans = Plan.objects.order_by('date')
    context = {'plans': plans}
    return render(request, 'meal_plans/plans.html', context)

def plan(request, plan_id):
    """Shows page of specific plan for selected day"""
    plan = Plan.objects.get(id=plan_id)
    fooditems = plan.fooditem_set.all().order_by('id')
    context = {'plan': plan, 'fooditems': fooditems}
    return render(request, 'meal_plans/plan.html', context)

def new_plan(request):
    """Add a new plan for acertain day"""
    FooditemFormset = formset_factory(NewFoodItem, extra=1)
    food_items = FoodItem.objects.all()


    if request.method != 'POST':
        # no data submitted; create blank form
        form = NewPlan()
        formset = FooditemFormset(prefix='food_items')

    else:
        # POST data submitted; process the data.
        form = NewPlan(request.POST)
        formset = FooditemFormset(request.POST, prefix='food_items')

        if form.is_valid():
            plan = form.save()
            # Handles grabbign the selcted food from the dropdown of food_items
            food_item_ids = request.POST.getlist('food_item')
            if food_item_ids:
                for food_id in food_item_ids:
                    foodItem = FoodItem.objects.get(id = food_id)
                    plan.fooditem_set.add(foodItem)

            # Handles the forms for new food items saved to database and plan
            if formset.is_valid():
                for food_form in formset:
                    food_item = food_form.save(commit=False)
                    food_item.save()
                    plan.fooditem_set.add(food_item)

            return redirect('meal_plans:plans')
        
    context = {'form': form, 'formset': formset, 'food_items':food_items}
    return render(request, 'meal_plans/new_plan.html', context)

def add_food_form(request):
    """Grabs the html content fomr food_form.html and returns a json response of it to be added to new_plan"""
    form = NewFoodItem()
    html = render(request, 'meal_plans/food_form.html', {'form': form}).content.decode('utf-8')
    return HttpResponse(html, content_type='text/plain; charset=utf-8')


def edit_plan(request, plan_id):
    """Edit an existing plan"""
    plan = Plan.objects.get(id=plan_id)

    if request.method != 'POST':
        form = NewPlan(instance=plan)
    
    else:
        form = NewPlan(instance=plan, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_plans/plans')
    context = {'form': form}
    return render(request, 'meal_plans/edit_plan.html', context)

def delete_plan(request, plan_id):
    """delete an existing plan and its contents"""
    plan = Plan.objects.get(id=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('meal_plans:plans')

    context = {'plan': plan}

    return render(request, 'meal_plans/delete_plan.html', context)

    
#  CHECK chatgpt for ideas on how to incorpoartae fatsecret