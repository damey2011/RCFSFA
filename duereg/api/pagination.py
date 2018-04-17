from rest_framework.pagination import CursorPagination


class ProgrammeInterestedAttendeePagination(CursorPagination):
    page_size = 10
