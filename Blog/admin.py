from django.contrib import admin

from .models import Comment, Post, Writer


# Register your models here.
admin.site.register(Writer)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields: {"slug":("title", )}
admin.site.register(Comment)