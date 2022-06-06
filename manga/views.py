from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from lists.models import List, ListItem
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
        if not request.user.is_authenticated:
            return redirect(reverse('accounts:login'))
        manga_pk = kwargs.get('pk')
        manga = get_object_or_404(Manga, pk=manga_pk)
        lists = set(manga.listitem_set.all().values_list('lista', flat=True))
        list = request.user.list_set.all().first()
        in_main_list = True if manga.id in list.listitem_set.all().values_list('manga_id', flat=True) else False
        return render(request, 'manga/details.html', {
            'manga': manga,
            'lists': lists,
            'in_main_list': in_main_list,
        })


@csrf_exempt
@login_required(login_url='/accounts/login/')
def toggle_to_list(request, manga_pk, list_pk):
    if request.method == "GET":
        print("ADD TO LIST TRIGGERED!")
        manga = get_object_or_404(Manga, pk=manga_pk)
        lista = get_object_or_404(List, pk=list_pk)
        existance = True if ListItem.objects.filter(manga=manga, lista=lista).exists() else False
        if existance:
            list_item = ListItem.objects.get(manga=manga, lista=lista)
            list_item.delete()
        else:
            lista.listitem_set.create(manga=manga)
        return JsonResponse({"message": "Success"}, status=200)
