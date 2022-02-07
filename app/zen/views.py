from django_filters.rest_framework import DjangoFilterBackend
from drf_psq import PsqMixin, Rule
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from .filters import ZenArticleBulkFilter
from .models import ZenArticle
from .serializers import ZenArticleAuthSerializer, ZenArticleNotAuthSerializer
from .pagination import ZenArticleBulkPagination


class ZenArticleBulkViewSet(PsqMixin, viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = ZenArticle.objects.distinct()
    pagination_class = ZenArticleBulkPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = ZenArticleBulkFilter


    # TODO: Запрашивать из бд только необходимые поля
    psq_rules = {
        ('retrieve', 'list'): [
            Rule([IsAuthenticated], ZenArticleAuthSerializer),
            Rule([AllowAny], ZenArticleNotAuthSerializer),
        ]
    }
