from rest_framework import serializers
from expenses.accounts.models import AssetAccount, ExpenseAccount, RevenueAccount


class AssetAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAccount
        fields = '__all__'


class ExpenseAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseAccount
        fields = '__all__'


class RevenueAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueAccount
        fields = '__all__'
