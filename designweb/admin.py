from django.contrib import admin
from designweb.models import UserProfile, Product, ProductExtension, Category, Order, OrderDetails, WishList, Cart
from django.utils.translation import ugettext_lazy

admin.site.site_header = ugettext_lazy('popdesign admin')
admin.site.site_title = ugettext_lazy('PopDesign')


class ExtensionProductInline(admin.StackedInline):
    model = ProductExtension


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'create_date', 'modified_date', 'price', 'is_active', )
    list_filter = ('create_date', 'price', 'is_active', )
    filter_horizontal = ('category', )
    ordering = ('-create_date', )

    inlines = [ExtensionProductInline, ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_date', 'modified_date', )
    list_filter = ('created_date', )
    ordering = ('category_name', )


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', )
    filter_horizontal = ('products', )


class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', )
    filter_horizontal = ('products', )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Cart, CartAdmin)