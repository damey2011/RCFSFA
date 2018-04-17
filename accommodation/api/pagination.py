from rest_framework.pagination import CursorPagination


class AccommodationPagination(CursorPagination):
    page_size = 10