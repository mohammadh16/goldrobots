from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('',include('pages.urls')),
    path('',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    )
