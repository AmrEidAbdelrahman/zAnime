from django.urls import path

from reviews.views import ReviewView

app_name = 'reviews'
urlpatterns = [
    path('<int:pk>/', ReviewView.as_view({'delete': 'destroy'}), name='delete'),
]
