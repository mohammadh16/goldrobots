from django.contrib import admin
from .models import Contract

class Contract_Admin(admin.ModelAdmin):
    list_display = ('id','name','minimum_deposit')
    list_display_links= ('id','name')
    search_fields = ('id','name')
admin.site.register(Contract,Contract_Admin)
