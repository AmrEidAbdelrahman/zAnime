from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from anime.views import Favlist

app_name = 'accounts'
urlpatterns = [
    path('favlist/', Favlist, name='fav-list'),
    path('profile/', user_views.profile, name='profile'),

    path('login/', user_views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='user/forget_password.html'), name='forgot-password'),
    path('register/', user_views.register, name='register'),
]
