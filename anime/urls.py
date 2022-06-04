from django.urls import path, include

from .views import add_to_fav, remove_from_fav, add_to_list, remove_from_list, \
    add_new_list, CommentView, ReviewView, edit_list, delete_list, IndexView

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view({'get': 'list'}), name='index'),

    # path('all-manga/', MangaListView.as_view({'get': 'list'}), name='all-manga'),

    # path('favlist/', Favlist, name='fav-list'),

    path('comment/', CommentView, name='comment'),
    # path('reply/', ReplyView, name='reply'),
    path('review/', ReviewView, name='submit-review'),

    path('add_to_fav/', add_to_fav, name='add-to-fav'),
    path('remove_from_fav/', remove_from_fav, name='remove-from-fav'),

    path('edit_list/<int:list_id>/', edit_list, name='edit-list'),
    path('add_new_list/', add_new_list, name='add-new-list'),
    path('add_to_list/', add_to_list, name='add-to-list'),
    path('remove_from_list/', remove_from_list, name='remove-from-list'),
    path('delete_list/', delete_list, name='delete-list'),
    path('latest-chapters/', IndexView.as_view({'get': 'latest_chapter'}), name='latest-chapters'),

    path('manga/', include('manga.urls', namespace='manga')),

    path('lists/', include('lists.urls')),
    # path('<str:manga_name>/', manga, name='manga'),
    # path('<str:manga_name>/', include('chapter.urls', namespace="chapters")),

]
