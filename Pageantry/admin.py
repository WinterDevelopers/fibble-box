from django.contrib import admin
from .models import *


class OfficeAdmin(admin.ModelAdmin):
    fields = ['pageantry', 'office_name']
    list_filter = ['pageantry']
    list_display = ['office_name']

# Register your models here.

admin.site.register(User)
admin.site.register(Pageantry)
admin.site.register(Candidate)
admin.site.register(Office, OfficeAdmin)
admin.site.register(votingCode)
admin.site.register(Payment)
admin.site.register(couponPayment)
admin.site.register(pageantrySponsor)