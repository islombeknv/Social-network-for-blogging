from django.contrib import admin

from account.models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = ['fullname', 'phone', 'address']
    search_fields = ['fullname', 'phone', 'address']
