from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from chapter.models import Chapter
from comments.forms import CommentForm
from manga.models import Manga


class ChapterView(ModelViewSet):
    queryset = Chapter.objects.all()

    def list(self, request, *args, **kwargs):
        return render(request, 'chapter/index.html', {})

    def retrieve(self, request, *args, **kwargs):
        chapter = self.get_object()
        return render(request, 'chapter/details.html', {
            'chapter': chapter,
        })


# def ChapterView(request, manga_name, chapter_number):
#     manga = Manga.objects.get(name=manga_name)
#     chapter = manga.chapter_set.get(chapter_number=chapter_number)
#     print(chapter.chapter_number)
#     all_chapter = manga.chapter_set.values_list('chapter_number', flat=True)
#     try:
#         imgs = chapter.imgs[1:-1]
#         imgs = imgs.split("\', \'")
#         imgs[0] = imgs[0][1:]
#         imgs[-1] = imgs[-1][:-2]
#     except:
#         imgs = None
#     form = CommentForm()
#
#     comments = chapter.comment_set.order_by("-pub_date").all()
#
#     context = {
#         'manga': manga,
#         'chapter': chapter,
#         'all_chapter': all_chapter,
#         'imgs': imgs,
#         'has_next': chapter.has_next(),
#         'has_pre': chapter.has_pre(),
#         'form': form,
#         'comments': comments,
#     }
#     return render(request, 'anime/chapter.html', context)
#
