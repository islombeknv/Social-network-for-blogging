from django.urls import path

from contacts.views import ContactCreateView, contact_send

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='create'),
    path('done/', contact_send),
]
