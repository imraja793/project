import user
from datetime import timedelta, date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from add_expense.forms import AddExpenseForm
from add_expense.models import AddExpense

@login_required
def add_expense(request):
    expense_added = False
    if request.method == 'POST':

        add_expense_form = AddExpenseForm(data=request.POST)
        if add_expense_form.is_valid():
            add_expense_form.save()
        expense_added = True
    else:
        add_expense_form = AddExpenseForm()

    return render(request, 'based/add_expense.html', {'add_expense_form': add_expense_form, 'expense_added': expense_added})

@login_required
def view_expense(request):
    expenses = AddExpense.objects.all()

    return render(request, 'based/view_expense.html', {'expenses': expenses})

@login_required
def get_expense(request, pk):
    expense = AddExpense.objects.get(id=pk)
    add_expense_form = AddExpenseForm(instance=expense)
    if add_expense_form.is_valid():
        print add_expense_form
    else:
        print 'Invalid'
    return render(request, 'based/edit_expense.html', {'add_expense_form': add_expense_form})

@login_required
def edit_expense(request, pk):
    expense = AddExpense.objects.get(id=pk)
    form = AddExpenseForm(request.POST, instance=expense)
    if form.is_valid():
        form.save()
    return render(request, 'based/edit_expense.html', {'editing': True})

@login_required
def date_find(request):
    samples = AddExpense.objects.filter(date__year='2018',
                          date__month='5')

    return render(request, 'based/date_change.html', {'samples': samples})



@login_required
def date_find_2(request):
    samples = AddExpense.objects.filter(date__range=["2018-05-14", "2018-06-27"])

    return render(request, 'based/date_find_2.html', {'samples': samples})



