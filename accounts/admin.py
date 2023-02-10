from django.contrib import admin
from accounts.models import Account


class Account_Admin(admin.ModelAdmin):
    list_display = ('id','accountname','accountid','registration_date')
    list_display_links= ('id','accountname')
    search_fields = ('accountname','accountid')

admin.site.register(Account, Account_Admin)



