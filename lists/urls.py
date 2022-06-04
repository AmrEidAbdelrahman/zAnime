from django.urls import path

from lists.views import MyListView

urlpatterns = [
    path('', MyListView.as_view({'get': 'list'}), name='mylist'),
    path('<str:name>/', MyListView.as_view({'get': 'retrieve'}), name='list-details'),
]
