from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import SocialAccount

class AdminAccount(UserAdmin):
    model=SocialAccount

    list_display=("email","username","is_active","is_superuser","last_login","date_joined")
    search_fields=("email","username")
    filter_horizontal=()
    list_filter=()
    readonly_fields=("last_login","date_joined")


admin.site.register(SocialAccount,AdminAccount)