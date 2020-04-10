from rest_framework import viewsets

from expenses.transactions.models import TransferTransaction, ExpenseTransaction, RevenueTransaction
from expenses.transactions.serializers import TransferTransactionSerializer, ExpenseTransactionSerializer, \
    RevenueTransactionSerializer


class TransferTransactionView(viewsets.ModelViewSet):
    serializer_class = TransferTransactionSerializer
    queryset = TransferTransaction.objects.all()


class ExpenseTransactionView(viewsets.ModelViewSet):
    serializer_class = ExpenseTransactionSerializer
    queryset = ExpenseTransaction.objects.all()


class RevenueTransactionView(viewsets.ModelViewSet):
    serializer_class = RevenueTransactionSerializer
    queryset = RevenueTransaction.objects.all()
