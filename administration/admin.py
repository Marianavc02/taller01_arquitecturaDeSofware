from django.contrib import admin
from .models import Alert, Computer,ComputerLog



# Register your models here.
admin.site.register(Alert)
admin.site.register(Computer)

@admin.register(ComputerLog)
class ComputerLogAdmin(admin.ModelAdmin):
    list_display = ("computer", "action", "timestamp")
    list_filter = ("action", "timestamp")
    search_fields = ("computer",)


