from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, ProductPriceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-prices', ProductPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
