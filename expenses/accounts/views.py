from rest_framework import viewsets

from expenses.accounts.models import AssetAccount, ExpenseAccount, RevenueAccount
from expenses.accounts.serializers import AssetAccountSerializer, ExpenseAccountSerializer, RevenueAccountSerializer
from expenses.core.mixins import AuthorizedViewMixin


class AssetAccountView(viewsets.ModelViewSet, AuthorizedViewMixin):
    serializer_class = AssetAccountSerializer
    queryset = AssetAccount.objects.all()


class ExpenseAccountView(viewsets.ModelViewSet, AuthorizedViewMixin):
    serializer_class = ExpenseAccountSerializer
    queryset = ExpenseAccount.objects.all()


class RevenueAccountView(viewsets.ModelViewSet, AuthorizedViewMixin):
    serializer_class = RevenueAccountSerializer
    queryset = RevenueAccount.objects.all()
