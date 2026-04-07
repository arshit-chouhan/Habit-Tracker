
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_habit, name='add_habit'),
    path('toggle/<int:log_id>/', views.toggle_habit, name='toggle_habit'),
    path('habit/<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
]
