from django.db import models

from expenses.accounts.models import AssetAccount, ExpenseAccount, RevenueAccount
from expenses.core.models import Currency


class Transaction(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, null=False)

    class Meta:
        abstract = True


class TransferTransaction(Transaction):
    source_account = models.ForeignKey(AssetAccount, related_name='transfer_negative_transactions',
                                       on_delete=models.DO_NOTHING, null=False)
    destination_account = models.ForeignKey(AssetAccount, related_name='transfer_positive_transactions',
                                            on_delete=models.DO_NOTHING, null=False)


class ExpenseTransaction(Transaction):
    source_account = models.ForeignKey(AssetAccount, related_name='expense_negative_transactions',
                                       on_delete=models.DO_NOTHING, null=False)
    destination_account = models.ForeignKey(ExpenseAccount, related_name='expense_positive_transactions',
                                            on_delete=models.DO_NOTHING, null=False)


class RevenueTransaction(Transaction):
    source_account = models.ForeignKey(RevenueAccount, related_name='revenue_negative_transactions',
                                       on_delete=models.DO_NOTHING, null=False)
    destination_account = models.ForeignKey(AssetAccount, related_name='revenue_positive_transactions',
                                            on_delete=models.DO_NOTHING, null=False)
