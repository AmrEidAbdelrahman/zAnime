from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', user_views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),

    path('notification/', user_views.NotificationView, name='notification'),

    path('profile/', user_views.profile, name='profile'),
    path('', include('anime.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
    urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)