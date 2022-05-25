from django.urls import path, include

from manga.views import MangaView

app_name = 'manga'
urlpatterns = [
    path('', MangaView.as_view({'get': 'list'}), name='index'),
    path('<int:pk>/', MangaView.as_view({'get': 'retrieve'}), name='details'),

    path('<int:pk>/chapters/', include('chapter.urls', namespace='chapter')),
]
