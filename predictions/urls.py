from rest_framework import routers
from .views import PredictionViewSet, StockViewSet, UserViewSet, UserStockViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'predictions', PredictionViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'users', UserViewSet)
router.register(r'user-stocks', UserStockViewSet)

urlpatterns = router.urls
