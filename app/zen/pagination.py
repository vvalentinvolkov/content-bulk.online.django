from rest_framework import pagination
from rest_framework.response import Response


class ZenArticleBulkPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'last_page': self.page.paginator.num_pages,
            'data': data
        })
