from django.contrib import admin
from .models import Avg_trade_quantity

class Avg_trade_quantity_Admin(admin.ModelAdmin):
    list_display = ('id','account','date','quantity')
    list_display_links= ('id','account')
    search_fields = ('id','account__accountname')
admin.site.register(Avg_trade_quantity,Avg_trade_quantity_Admin)

