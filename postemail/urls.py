from django.urls import path

from postemail.views import EmailCreateView

app_name = 'email'

urlpatterns = [
    path('', EmailCreateView.as_view(), name='create')
]
