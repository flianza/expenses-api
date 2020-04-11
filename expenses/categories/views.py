from rest_framework import viewsets

from expenses.categories.models import Category
from expenses.categories.serializers import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
