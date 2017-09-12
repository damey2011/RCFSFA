from rest_framework.pagination import CursorPagination


class LikePagination(CursorPagination):
    page_size = 10
    ordering = 'timestamp'
