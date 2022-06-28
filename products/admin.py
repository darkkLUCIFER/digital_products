from django.contrib import admin
from .models import Category, Product, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'title', 'active', 'created',)
    list_filter = ('active', 'parent',)
    search_fields = ('title',)


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ('title', 'file_type', 'file', 'active')
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created',)
    list_filter = ('active',)
    search_fields = ('title',)
    filter_horizontal = ('categories',)
    inlines = (FileInlineAdmin,)
