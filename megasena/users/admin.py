from django.contrib import admin

from users.models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Users)
