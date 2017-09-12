from django.contrib import admin

# Register your models here.
from logs.models import LoginLog

admin.site.register(LoginLog)
