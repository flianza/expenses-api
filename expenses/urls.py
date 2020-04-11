from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from expenses.accounts.views import AssetAccountView, ExpenseAccountView, RevenueAccountView
from expenses.categories.views import CategoryView
from expenses.core.views import CurrencyView
from expenses.transactions.views import TransferTransactionView, ExpenseTransactionView, RevenueTransactionView
from expenses.users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'currencies', CurrencyView)
router.register(r'accounts/asset', AssetAccountView)
router.register(r'accounts/expense', ExpenseAccountView)
router.register(r'accounts/revenue', RevenueAccountView)
router.register(r'transactions/asset', TransferTransactionView)
router.register(r'transactions/expense', ExpenseTransactionView)
router.register(r'transactions/revenue', RevenueTransactionView)
router.register(r'categories', CategoryView)

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('api/', include(router.urls)),
        path('api-token-auth/', views.obtain_auth_token),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
