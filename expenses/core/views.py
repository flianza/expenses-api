from rest_framework import viewsets

from expenses.core.models import Currency
from expenses.core.serializers import CurrencySerializer


class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
