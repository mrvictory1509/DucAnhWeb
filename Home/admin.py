from django.contrib import admin
from .models import Category, Vests, CartUser, BillUser

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Description']
    list_filter = ['Name']
    search_fields = ['Name']
admin.site.register(Category, CategoryAdmin)

class VestsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Price', 'CategoryID', 'NumberBuy', 'Made_in', 'Sales', 'New_Price', 'Image', 'Description']
    list_filter = ['CategoryID']
    search_fields = ['CategoryID']
admin.site.register(Vests, VestsAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['VestsID', 'Quantity', 'UserID']
    list_filter = ['VestsID']
    search_fields = ['VestsID']
admin.site.register(CartUser, CartAdmin)

class SetBillAdmin(admin.ModelAdmin):
    list_display = ['Date', 'UserID', 'Image', 'Ship']
    list_filter = ['UserID']
    search_fields = ['UserID']
admin.site.register(BillUser, SetBillAdmin)