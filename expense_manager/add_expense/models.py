from __future__ import unicode_literals

from django.contrib import auth
from django.db import models

from django.core.validators import MaxValueValidator, RegexValidator


class Payments(models.Model):

        paymen = models.CharField(max_length=30, blank=True, null=True)

        def __str__(self):
            return self.paymen

class Expenses(models.Model):

        expen = models.CharField(max_length=30, blank=True, null=True)

        def __str__(self):
            return self.expen


class AddExpense(models.Model):
    expense_title = models.CharField('Expense Title', max_length=20)
    amount = models.DecimalField('Amount', decimal_places=2, max_digits=10)
    currency = models.CharField('Currency', max_length=23)
    vendor_name = models.CharField('Vendor Name', max_length=200, blank=True)
    last4digit = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$')])
    invoice = models.IntegerField()
    userid = models.IntegerField()
    date = models.DateField()
    payment_type = models.ForeignKey(Payments)
    expense_type = models.ForeignKey(Expenses)






