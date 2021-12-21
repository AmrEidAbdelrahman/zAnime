from django.urls import path, include
from .views import index, manga, MangaListView, add_to_fav, remove_from_fav, add_to_list, remove_from_list, add_new_list, Lists, ListDetails, Favlist, ChapterView, CommentView

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('manga/', MangaListView.as_view(), name='all-manga'),
    path('manga/<str:manga_name>/<int:chapter_number>/', ChapterView, name='chapter'),
    path('lists/', Lists, name='mylist'),
    path('favlist/', Favlist, name='fav-list'),
    path('listdetails/<str:list_name>/', ListDetails, name='list-details'),

    path('comment/', CommentView, name='comment'),

    path('add_to_fav/', add_to_fav, name='add-to-fav'),
    path('remove_from_fav/', remove_from_fav, name='remove-from-fav'),
    path('add_new_list/', add_new_list, name='add-new-list'),

    path('add_to_list/', add_to_list, name='add-to-list'),
    path('remove_from_list/', remove_from_list, name='remove-from-list'),

    path('<str:manga_name>/', manga, name='manga'),
]
