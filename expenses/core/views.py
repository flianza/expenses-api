from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from expenses.core.mixins import AuthorizedViewMixin
from expenses.core.models import Currency
from expenses.core.serializers import CurrencySerializer, CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CurrencyView(viewsets.ModelViewSet, AuthorizedViewMixin):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
