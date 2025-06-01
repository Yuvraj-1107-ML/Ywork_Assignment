from django.contrib import admin
from .models import Item



#admin.site.register(Item)
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'title', 'description')
    search_fields = ('username', 'title')
