from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import SocialAccount

class AdminAccount(UserAdmin):
    model=SocialAccount

    search_fields=('email','username')
    ordering=['-date_joined']
    list_display=('email','username','is_active','is_superuser','last_login')
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('profile_picture','background_picture')}),
    )
    


admin.site.register(SocialAccount,AdminAccount)