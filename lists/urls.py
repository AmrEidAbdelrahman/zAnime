from django.urls import path

from lists.views import MyListView

app_name = 'lists'
urlpatterns = [
    path('', MyListView.as_view({'get': 'list'}), name='mylist'),
    path('add_new_list/', MyListView.as_view({'post': 'create'}), name='create-list'),
    path('<int:id>/update/', MyListView.as_view({'post': 'update'}), name='update'),
    path('<str:name>/', MyListView.as_view({'get': 'retrieve'}), name='list-details'),

]
