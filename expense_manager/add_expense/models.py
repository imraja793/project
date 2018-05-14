from __future__ import unicode_literals


from django.db import models


class AddExpense(models.Model):
    expense_title = models.CharField('Expense Title', max_length=20)
    amount = models.DecimalField('Amount', decimal_places=2, max_digits=10)
    currency = models.CharField('Currency', max_length=23)
    vendor_name = models.CharField('Vendor Name', max_length=200, blank=True)
    last4digit = models.IntegerField()
    invoice = models.IntegerField()
    userid = models.IntegerField()

#
#     payment_type = models.ForeignKey(Payment5)
#     expense_type = models.ForeignKey(Expense3)