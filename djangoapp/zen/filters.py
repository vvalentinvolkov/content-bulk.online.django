import django_filters
from django.db import models
from django.db.models import Q, Count
from django_filters import rest_framework as filters, BaseInFilter, CharFilter, BaseRangeFilter, NumberFilter

from .models import ZenArticle, ZenFeed


class NumberRangeFilter(BaseRangeFilter, NumberFilter):
    pass


class CharInFilter(BaseInFilter, CharFilter):
    pass


class ZenArticleBulkFilter(filters.FilterSet):

    feeds = CharInFilter(field_name='feeds__name', lookup_expr='in')

    class Meta:
        model = ZenArticle
        filter_overrides = {
            models.IntegerField: {
                'filter_class': NumberRangeFilter,
                'extra': lambda f: {
                    'lookup_expr': 'range',
                },
            },
        }
        exclude = ['link, id']

