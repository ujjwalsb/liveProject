from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
    )


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2           # No of api per page
    max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
    page_size = 10               # No of api per page