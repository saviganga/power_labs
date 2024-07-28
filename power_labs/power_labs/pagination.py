from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PowerLabsPagination(PageNumberPagination):
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        dt = {
            "status": "SUCCESS",
            "message": "Successfully fetched data",
            "count": count,
            "next": next_url,
            "previous": previous_url,
            "data": data,
        }
        return Response(dt)
