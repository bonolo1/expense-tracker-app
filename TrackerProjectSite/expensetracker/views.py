from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateExpenseForm
from .models import Expense
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth, TruncDate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    View function renders the home page

    :param request: HTTP request made using url root

    :returns: renders expensetracker/home.html as response
    """

    return render(request, 'expensetracker/home.html')

@login_required (login_url='user_auth:login')
def view_list(request):
    """
    View function renders the list of expenses

    :param request: HTTP request made using url view_expense_list/

    :returns: renders expensetracker/expense_list.html as response
    """
    Expense_list = Expense.objects.all().order_by('date')
    context = {'Expense_list': Expense_list}
    return render (request, 'expensetracker/expense_list.html', context)

@login_required (login_url='user_auth:login')
def log_expense(request):
    """
    View function enables user to input expense transaction

    :param request: HTTP request made using url log_expense/

    :returns: redirects user to url view_expense_list/ as response if input is valid

    :raises request: renders expensetracker/expense_input.html if input is invalid
    """
    expense_form = CreateExpenseForm(request.POST)
    if request.method =='POST':
        expense_form = CreateExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('expensetracker:view_list')
    else:
        expense_form = CreateExpenseForm()
    context = {'expense_form': expense_form}    
    return render(request, 'expensetracker/expense_input.html', context)


# Function to show the summary calculations of expenses tracked in different groups/views, including total expense, subtotals by categores
# and by month
@login_required (login_url='user_auth:login')
def expense_calculations(request):
    """
    View function renders a summary of various expense transaction information

    :param request: HTTP request made using url expense_summary/

    :returns: renders expensetracker/expense_summary.html as response
    """
    total_expense = Expense.objects.aggregate(Sum('expense_amount'))

    all_expense_objects = Expense.objects.all()
    total_expense_by_category = Expense.objects.values('category_descr').annotate(category_totals= Sum('expense_amount'), category_count_of_items_with_category= Count('category_descr'))

    total_expense_by_month = Expense.objects.annotate(month=TruncMonth('date')).values('month').annotate(month_totals= Sum('expense_amount'))

    total_expense_by_day = Expense.objects.values('date').annotate(day_totals= Sum('expense_amount'))

    context ={'total_expense': total_expense['expense_amount__sum'],
            'total_expense_by_category': total_expense_by_category,
            'all_expense_objects': all_expense_objects,
            'total_expense_by_month': total_expense_by_month,
            'total_expense_by_day': total_expense_by_day
            }
    return render(request, 'expensetracker/expense_summary.html', context)