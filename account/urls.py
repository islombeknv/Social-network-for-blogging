from django.urls import path

from account.views import AccountUpdateView

app_name = 'account'

urlpatterns = [
    path('', AccountUpdateView.as_view(), name='update'),
]