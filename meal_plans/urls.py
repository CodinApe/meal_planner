"""define url patterns for meal_plans"""

from django.urls import path

from . import views

app_name = 'meal_plans'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    path('plans/', views.plans, name='plans'),

    path('plans/<int:plan_id>/', views.plan, name = 'plan'),

    path('new_plan/', views.new_plan, name='new_plan'),

    path('add_food_form/', views.add_food_form, name='add_food_form'),

    path('edit_plan/', views.edit_plan, name='edit_plan'),

    path('delete_plan/<int:plan_id>/', views.delete_plan, name='delete_plan'),

    path('plans_for_date', views.plans_for_date, name='plans_for_date'),

    path('food_items', views.food_items, name='food_items'),

    path('goal', views.goal, name='goal'),

    path('create_goal/<int:goal_id>/', views.create_goal, name='create_goal'), 
    

]