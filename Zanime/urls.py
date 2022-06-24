from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('notification/', user_views.NotificationView, name='notification'),

    path('accounts/', include('user.urls', namespace='accounts')),
    path('', include('anime.urls', namespace='main')),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
