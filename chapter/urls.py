from django.urls import path

from chapter.views import ChapterView

app_name = "chapter"

urlpatterns = [
    path('', ChapterView.as_view({'get': 'list'}), name='latest'),
    path('<int:chapter_pk>/', ChapterView.as_view({'get': 'retrieve'}), name='details'),
]
