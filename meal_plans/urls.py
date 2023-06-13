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
]