from django.contrib import admin
from .models import Payment_history


class Payment_Admin(admin.ModelAdmin):
    list_display = ('id','account','date','amount')
    list_display_links= ('id','account')
    search_fields = ('id','account__accountname')
admin.site.register(Payment_history,Payment_Admin)