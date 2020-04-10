from django.db import models
from expenses.core.models import Currency


class Account(models.Model):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    initial_balance = models.FloatField(default=0)

    class Meta:
        abstract = True


class AssetAccount(Account):
    cbu = models.CharField(max_length=100, null=True)
    alias_cbu = models.CharField(max_length=17, null=True)


class RevenueAccount(Account):
    pass


class ExpenseAccount(Account):
    pass
