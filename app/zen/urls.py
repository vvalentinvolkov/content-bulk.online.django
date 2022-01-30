from rest_framework import routers

from .views import ZenArticleBulkViewSet

router = routers.SimpleRouter()
router.register(r'zen_articles', ZenArticleBulkViewSet)
urlpatterns = router.urls
