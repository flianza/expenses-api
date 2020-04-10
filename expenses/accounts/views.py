from rest_framework import viewsets
from expenses.accounts.models import AssetAccount, ExpenseAccount, RevenueAccount
from expenses.accounts.serializers import AssetAccountSerializer, ExpenseAccountSerializer, RevenueAccountSerializer


class AssetAccountView(viewsets.ModelViewSet):
    serializer_class = AssetAccountSerializer
    queryset = AssetAccount.objects.all()


class ExpenseAccountView(viewsets.ModelViewSet):
    serializer_class = ExpenseAccountSerializer
    queryset = ExpenseAccount.objects.all()


class RevenueAccountView(viewsets.ModelViewSet):
    serializer_class = RevenueAccountSerializer
    queryset = RevenueAccount.objects.all()
