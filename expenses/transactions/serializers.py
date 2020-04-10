from rest_framework import serializers

from expenses.transactions.models import TransferTransaction, ExpenseTransaction, RevenueTransaction


class TransferTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferTransaction
        fields = '__all__'


class ExpenseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTransaction
        fields = '__all__'


class RevenueTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueTransaction
        fields = '__all__'
