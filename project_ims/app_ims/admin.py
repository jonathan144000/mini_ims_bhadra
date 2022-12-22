from django.contrib import admin
from .models import Category, Item, AppUser

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category",)

class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "particular","category", "ledger_folio", "quantity", "price", "total", "entry_date")
    list_filter = ("title","category")
    search_fields = ("title", "entry_date")

class AppUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name", "email")

admin.site.register(Category, CategoryAdmin)
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Item, ItemAdmin)

admin.site.site_title = "Admin"
admin.site.index_title = "Dashboard"
admin.site.site_header = "MINI IMS"