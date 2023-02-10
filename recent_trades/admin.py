from django.contrib import admin
from .models import Recent_Trades

class Recent_trades_Admin(admin.ModelAdmin):
    list_display = ('id','account','type')
    list_display_links= ('id','account')
    search_fields = ('id','account__accountname','type')
admin.site.register(Recent_Trades,Recent_trades_Admin)