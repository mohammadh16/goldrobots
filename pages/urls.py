from django.urls import path


from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contract',views.contract, name='contract'),
    path('investment',views.investment, name='investment'),
    path('news',views.news, name='news'),
    path('bank',views.bank, name='bank'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('contractprofit',views.contractprofit, name='contractprofit'),
    path('profile',views.profile, name='profile'),
    path('setting',views.setting, name='setting'),
    path('logout',views.logout, name='logout'),
]