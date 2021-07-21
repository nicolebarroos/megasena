from django.contrib import admin

from game.models import Plays

class PlaysAdmin(admin.ModelAdmin):
    list_display = ['results']

admin.site.register(Plays)
