from django.forms import ModelForm
from .models import Expense
from django import forms

# Enable a datepicker for the date field in the form.
# Ref: https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d %b %Y'

# Create form where user can record their expenses
class CreateExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'item_description', 'category_descr', 'expense_amount']
        widgets = {'date': DateInput()}