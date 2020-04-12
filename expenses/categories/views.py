from rest_framework import viewsets

from expenses.categories.models import Category
from expenses.categories.serializers import CategorySerializer
from expenses.core.mixins import AuthorizedViewMixin


class CategoryView(viewsets.ModelViewSet, AuthorizedViewMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
