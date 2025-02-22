from django.contrib import admin
from .models import (
    ProductModel,
    CategoryModel,
    ProductImageModel,
    WishListModel,
)


# @admin.register(ProductModel)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "title",
#         "price",
#         "discount_percent",
#         "stock",
#         "status",
#     )


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title',  'price', 'stock', 'status', 'created_date')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generates slug from title

admin.site.register(ProductModel, ProductModelAdmin)


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}  # Auto-populates slug from title

admin.site.register(CategoryModel, CategoryModelAdmin)


@admin.register(ProductImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product")


@admin.register(WishListModel)
class WishListAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
