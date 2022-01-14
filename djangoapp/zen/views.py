from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import ZenArticle
from .serializers import ZenArticleSerializer


class ZenArticleBulkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = ZenArticle.objects.all()
    serializer_class = ZenArticleSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['feeds__name']
