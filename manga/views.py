from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from manga.models import Manga


class MangaView(ModelViewSet):
    queryset = Manga.objects.all()
    pagination_class = LimitOffsetPagination
    pagination_by = 15

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        manga_list = Paginator(qs, self.pagination_by)
        page = request.GET.get('page', 1)
        manga_list = manga_list.get_page(page)
        return render(request, 'manga/index.html', {
            'manga_list': manga_list
        })

    def retrieve(self, request, *args, **kwargs):
        manga_pk = kwargs.get('pk')
        manga = get_object_or_404(Manga, pk=manga_pk)
        lists = set(manga.listitem_set.all().values_list('lista', flat=True))
        list = request.user.list_set.all().first()
        in_main_list = True if list.id in manga.listitem_set.all().values_list('lists', flat=True) else False
        print(in_main_list)
        return render(request, 'manga/details.html', {
            'manga': manga,
            'lists': lists
        })
