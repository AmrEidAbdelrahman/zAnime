from django.urls import path, include

from manga.views import MangaView, toggle_to_list

app_name = 'manga'
urlpatterns = [
    path('', MangaView.as_view({'get': 'list'}), name='index'),
    path('<int:pk>/', MangaView.as_view({'get': 'retrieve'}), name='details'),
    path('<int:manga_pk>/toggle_to_list/<int:list_pk>/', toggle_to_list, name='add-to-list'),
    path('<int:pk>/chapters/', include('chapter.urls', namespace='chapter')),
]
