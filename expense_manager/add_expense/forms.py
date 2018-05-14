from django import forms

from add_expense.models import AddExpense

class AddExpenseForm(forms.ModelForm):

    class Meta:
        model = AddExpense
        fields = '__all__'