from django.contrib import admin

from expenses.transactions.models import TransferTransaction, ExpenseTransaction, RevenueTransaction

admin.site.register(TransferTransaction)
admin.site.register(ExpenseTransaction)
admin.site.register(RevenueTransaction)
