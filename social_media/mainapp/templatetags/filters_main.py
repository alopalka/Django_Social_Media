from django import template

from user.models import SocialAccount

register=template.Library()

@register.filter
def photo_filter(account):
    current_user=SocialAccount.objects.get(username=account)
    if current_user.profile_picture:
        return current_user.profile_picture.url
    else:
        return '/static/img/mainapp/user.png'
    