from django.contrib import admin
from .models import Post, Category


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)
nullfy_quantity.short_description = 'Удалить статью'


class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_type', 'date_in', 'rating')
    list_filter = ('author', 'post_type', 'date_in', 'rating')
    search_fields = ('author', 'post_type')
    actions = [nullfy_quantity]


admin.site.register(Category)
admin.site.register(Post, PostsAdmin)