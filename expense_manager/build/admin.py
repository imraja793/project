from django.contrib import admin

from .models import UserProfileInfo, User
from add_expense.models import AddExpense, Payments, Expenses

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(AddExpense)
admin.site.register(Payments)
admin.site.register(Expenses)
