from django.contrib import admin

from .models import UserProfileInfo, User
from add_expense.models import AddExpense

# Register your models here.
admin.site.register(AddExpense)
