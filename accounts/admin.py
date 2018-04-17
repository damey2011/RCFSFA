from django.contrib import admin

# Register your models here.
from accounts.models import MemberProfile, CoordinatorProfile, ExcoProfile, UserRole, AccountCreationTokens

admin.site.register(MemberProfile)
admin.site.register(CoordinatorProfile)
admin.site.register(ExcoProfile)
admin.site.register(UserRole)
admin.site.register(AccountCreationTokens)
