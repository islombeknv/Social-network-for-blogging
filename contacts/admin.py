from django.contrib import admin

from contacts.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = ['name', 'email', 'company', 'select']
    search_fields = ['name', 'email', 'company', 'select']