from django.contrib import admin

from .models import Comment, Post, Writer


# Register your models here.
@admin.register(Writer)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name")
    prepopulated_fields = {"slug": ("first_name", "last_name")}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("writer",)
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Comment)