import logging

from django_filters.rest_framework import DjangoFilterBackend
from drf_psq import PsqMixin, Rule
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .filters import ZenArticleBulkFilter
from .models import ZenArticle
from .serializers import ZenArticleAuthSerializer, ZenArticleNotAuthSerializer
from .pagination import ZenArticleBulkPagination

logger = logging.getLogger(__name__)


class ZenArticleBulkViewSet(PsqMixin, viewsets.ModelViewSet):
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
        ],
        ('create', 'update', 'partial_update', 'destroy'): [
            Rule([IsAdminUser], ZenArticleAuthSerializer),
        ]
    }
