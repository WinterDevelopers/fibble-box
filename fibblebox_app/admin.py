from django.contrib import admin
from .models import *


class OfficeAdmin(admin.ModelAdmin):
    fields = ['event', 'office_name']
    list_filter = ['event']
    list_display = ['office_name']

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Candidate)
admin.site.register(Office, OfficeAdmin)
admin.site.register(votingCode)
admin.site.register(Payment)