from django.contrib import admin

from .models import Comment, Post, Writer


# Register your models here.
class WriterAdmin(admin.ModelAdmin):
    list_display = ( "first_name", "last_name")
    prepopulated_fields = {"slug": ("first_name", "last_name")}

admin.site.register(Writer, WriterAdmin)


class PostAdmin(admin.ModelAdmin):
    list_filter = ("writer",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)


admin.site.register(Comment)