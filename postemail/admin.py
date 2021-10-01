from django.contrib import admin

from postemail.models import EmailModel


@admin.register(EmailModel)
class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['email']
    list_filter = ['created_at']

