from django import template
from online_users.models import OnlineUserActivity

register = template.Library()


@register.simple_tag
def get_online(request):
    return OnlineUserActivity.get_user_activities()



