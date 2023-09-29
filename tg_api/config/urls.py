from django.contrib import admin
from django.urls import path, include

from apps.bot.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('bot/', include('apps.bot.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

urlpatterns += doc_urls
