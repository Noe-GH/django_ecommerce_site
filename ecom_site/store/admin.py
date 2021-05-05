from django.contrib import admin
from .models import Product, Order

admin.site.site_header = 'EcomSite'
admin.site.site_title = 'EcomSite'
admin.site.index_title = 'EcomSite administration'

class ProductAdmin(admin.ModelAdmin):
    def set_category_to_default(self, request, queryset):
        queryset.update(category='default')

    set_category_to_default.short_description = 'Category to default'
    list_display = ('name', 'price', 'price_discount', 'category', 'description',)
    search_fields = ('title',)
    actions = ('set_category_to_default',)
    fields = ('name', 'price', 'image',)
    list_editable = ('price_discount',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
