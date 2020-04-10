from django.contrib import admin
from expenses.accounts.models import AssetAccount, ExpenseAccount, RevenueAccount


admin.site.register(AssetAccount)
admin.site.register(ExpenseAccount)
admin.site.register(RevenueAccount)
