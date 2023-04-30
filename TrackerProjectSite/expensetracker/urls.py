from django.urls import path
from . import views

app_name ='expensetracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('view_expense_list/', views.view_list, name='view_list'),
    path('log_expense/', views.log_expense, name='log_expense'),
    path('expense_summary/', views.expense_calculations, name='expense_calculations')
]
