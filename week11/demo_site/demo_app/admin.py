from django.contrib import admin
from demo_app.models import Event, KeyWord


class EventAdmin(admin.ModelAdmin):
    pass


class KeyWordAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(KeyWord, KeyWordAdmin)
