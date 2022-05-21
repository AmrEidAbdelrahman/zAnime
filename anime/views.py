from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination

from chapter.models import Chapter
from comments.forms import CommentForm
from comments.models import Comment
from manga.models import Manga
from reviews.forms import ReviewForm
from reviews.models import Review
from user.models import Favorit, List, ListItem
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet

# Create your views here.


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def testview(request, room_name='event'):
    print("##########TESTVIEW###########")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'event_amr',
        {
            'type': 'receive',
            'message': 'message_dsadsa'
        }
    )
    print("########AFTER TEST VIEW#########")
    context = {
        'a': 'a',
    }
    return render(request, 'anime/test.html', context)


class IndexView(ModelViewSet):
    model = Manga
    paginated_by = 10
    queryset = Manga.objects.all()[:10]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        context = {
            'manga': qs,
            'tab': 'home',
        }
        return render(request, 'anime/index.html', context)


def manga(request, manga_name):
    manga = get_object_or_404(Manga, title=manga_name)
    user = request.user
    fav_manga = user.favorit_set.values_list('manga', flat=True)
    lists = user.list_set.all()
    in_fav = True if manga.id in fav_manga else False

    lista = user.list_set.all().first()
    if lista:
        manga_in_the_list = lista.listitem_set.values_list('manga', flat=True)
        in_list = True if manga.id in manga_in_the_list else False
    else:
        in_list = False
    listitems = []
    listas = user.list_set.all()
    for l in listas:
        manga_in_the_list = list(l.listitem_set.values_list('manga', flat=True))
        listitems.append(manga_in_the_list)

    chapters = None
    try:
        chapters = manga.chapter_set.all()
    except Exception as e:
        print(e)

    form = ReviewForm()

    context = {
        'manga': manga,
        'chapters': chapters,
        'in_fav': in_fav,
        'lists': lists,
        'listitems': listitems,
        'in_list': in_list,
        'tab': 'manga',
        'form': form
    }
    return render(request, 'anime/manga.html', context)


class MangaListView(ModelViewSet):
    model = Manga
    order_by = '-rate'
    paginated_by = 15
    pagination_class = LimitOffsetPagination

    queryset = Manga.objects.all()

    def list(self, reqeust, *args, **kwargs):
        qs = self.get_queryset()
        paginator = Paginator(qs, self.paginated_by)
        page = reqeust.GET.get('page', 1)
        manga = paginator.get_page(page)
        context = {
            'manga_list': manga,
            'tab': 'manga',
        }
        return render(reqeust, 'anime/all_manga.html', context)

@login_required(login_url='/login/')
def add_to_fav(request):
    if request.method == "POST":
        try:
            manga_id = request.POST.get('manga_id')
            manga = Manga.objects.get(pk=manga_id)
            user = request.user

            fav_manga = Favorit(user=user, manga=manga)
            fav_manga.save()
            data = {
                'manga_name': 'manga.name'
            }

            return JsonResponse(data, status=200)
        except Exception as e:
            print("crap2")
            return JsonResponse({"error": "str(e)"}, status=404)


@login_required(login_url='/login/')
def remove_from_fav(request):
    if request.method == "POST":
        try:
            manga_id = request.POST.get('manga_id')
            manga = Manga.objects.get(pk=manga_id)
            user = request.user

            fav_manga = Favorit.objects.filter(user=user, manga=manga)
            fav_manga[0].delete()
            data = {
                'manga_name': 'manga.name'
            }

            return JsonResponse(data, status=200)
        except Exception as e:
            print("crap2")
            return JsonResponse({"error": str(e)}, status=404)


@login_required(login_url='/login/')
def add_to_list(request):
    if request.method == "POST":
        try:
            manga_id = request.POST.get('manga_id')
            list_name = request.POST.get('list_name')
            manga = Manga.objects.get(pk=manga_id)
            user = request.user
            lista = List.objects.get(user=user, name=list_name)
            listitem = ListItem.objects.filter(lista=lista, manga=manga)
            if listitem:
                pass
            else:
                listitem = ListItem(lista=lista, manga=manga)
                print("what ........")
                listitem.save()
            data = {
                'manga_name': 'manga.name',
                'list_js': None,
            }
            return JsonResponse(data, status=200)
        except Exception as e:
            print("crap2")
            return JsonResponse({"error": str(e)}, status=404)


'''
'''


@login_required(login_url='/login/')
def remove_from_list(request):
    if request.is_ajax and request.method == "POST":
        try:
            manga_id = request.POST.get('manga_id')
            list_name = request.POST.get('list_name')
            manga = Manga.objects.get(pk=manga_id)
            user = request.user
            lista = List.objects.get(user=user, name=list_name)
            listitem = ListItem.objects.get(lista=lista, manga=manga)
            if listitem:
                listitem.delete()
            data = {
                'manga_name': 'manga.name'
            }

            return JsonResponse(data, status=200)
        except Exception as e:
            print("crap2")
            return JsonResponse({"error": str(e)}, status=404)


@login_required(login_url='/login/')
def add_new_list(request):
    if request.method == "POST":
        try:
            new_list = request.POST.get('new_option')
            user = request.user
            lista = None
            try:
                lista = List.objects.get(user=user, name=new_list)
            except:
                pass

            if lista:
                pass
            else:
                list_ = List(user=user, name=new_list)
                print("what ........")
                list_.save()

            return JsonResponse({"new_list": new_list}, status=200)
        except Exception as e:
            print("crap2")
            return JsonResponse({"error": str(e)}, status=404)


# @login_required(login_url='/login/')
# def Lists(request):
#     user = request.user
#
#     lists_ = user.list_set.all()
#     paginator = Paginator(lists_, 5)  # Show 25 contacts per page.
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     print(lists_)
#     context = {
#
#         'tab': 'lists',
#         'page_obj': page_obj,
#     }
#     return render(request, 'anime/lists.html', context)


class MyListView(ModelViewSet):
    model = List
    paginated_by = 10
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        return user.list_set.all()

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        page = request.GET.get('page', 1)
        paginator = Paginator(qs, self.paginated_by)
        lists = paginator.get_page(page)
        context = {
            'lists': lists ,
            'tab': 'lists',
        }
        return render(request, 'anime/lists.html', context)


@login_required(login_url='/login/')
def ListDetails(request, list_name):
    user = request.user
    lista = List.objects.get(user=user, name=list_name)
    list_items = lista.listitem_set.all()

    paginator = Paginator(list_items, 15)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'list_name': list_name,
        'tab': 'lists',
        'page_obj': page_obj,
    }
    return render(request, 'anime/list.html', context)


@login_required(login_url='/login/')
def edit_list(request, list_id):
    if request.is_ajax and request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        try:
            list_ = List.objects.get(pk=list_id)
            list_.name = name
            list_.save()
            print("WE ARE  HERE !!!")
            print(list_.name)
            return JsonResponse({"new_list": "edited"}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"new_list": "new_list"}, status=404)


@login_required(login_url='/login/')
def delete_list(request):
    if request.is_ajax and request.method == "POST":
        user = request.user
        list_id = request.POST.get('list_id')
        try:
            list_ = List.objects.get(pk=list_id, user=user)
            list_.delete()
            print("WE ARE  HERE !!!")
            return JsonResponse({"status": "deleted"}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"new_list": "new_list"}, status=404)


@login_required(login_url='/login/')
def Favlist(request):
    user = request.user
    fav_items = user.favorit_set.all()

    paginator = Paginator(fav_items, 15)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        'tab': 'fav',
        'page_obj': page_obj,
    }
    return render(request, 'anime/list.html', context)


def ChapterView(request, manga_name, chapter_number):
    manga = Manga.objects.get(name=manga_name)
    chapter = manga.chapter_set.get(chapter_number=chapter_number)
    print(chapter.chapter_number)
    all_chapter = manga.chapter_set.values_list('chapter_number', flat=True)
    try:
        imgs = chapter.imgs[1:-1]
        imgs = imgs.split("\', \'")
        imgs[0] = imgs[0][1:]
        imgs[-1] = imgs[-1][:-2]
    except:
        imgs = None
    form = CommentForm()

    comments = chapter.comment_set.order_by("-pub_date").all()

    context = {
        'manga': manga,
        'chapter': chapter,
        'all_chapter': all_chapter,
        'imgs': imgs,
        'has_next': chapter.has_next(),
        'has_pre': chapter.has_pre(),
        'form': form,
        'comments': comments,
    }
    return render(request, 'anime/chapter.html', context)


@login_required(login_url='/login/')
def CommentView(request):
    if request.is_ajax and request.method == "POST":
        try:
            content = request.POST.get('content')
            manga_name = request.POST.get("manga_name")
            chapter_number = request.POST.get("chapter_number")
            manga = Manga.objects.get(name=manga_name)
            chapter = Chapter.objects.get(manga=manga, chapter_number=chapter_number)
            user = request.user

            comment = Comment(user=user, chapter=chapter, content=content)
            comment.save()

            data = {
                'username': user.username,
            }

            return JsonResponse(data, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=404)


#
# @login_required(login_url='/login/')
# def ReplyView(request):
#     if request.is_ajax and request.method == "POST":
#         try:
#             content = request.POST.get('content')
#             comment_id = request.POST.get("comment_id")
#             user = request.user
#             comment = Comment.objects.get(pk=comment_id)
#
#             reply = Reply(user=user, comment=comment, content=content)
#             print(reply)
#             reply.save()
#
#             data = {
#                 'username': user.username,
#             }
#
#             return JsonResponse(data, status=200)
#         except Exception as e:
#             print(e)
#             return JsonResponse({"error": str(e)}, status=404)


@login_required(login_url='/login/')
def ReviewView(request):
    if request.is_ajax and request.method == "POST":
        try:
            content = request.POST.get('content')
            rate = request.POST.get("rate")
            manga_id = request.POST.get("manga_id")
            user = request.user
            manga = Manga.objects.get(pk=manga_id)

            review = Review(user=user, manga=manga, content=content, given_rate=rate)
            print(review)
            review.save()

            data = {

            }
            return JsonResponse(data, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=404)


'''
def notification_test_page(request):

    # Django Channels Notifications Test
    current_user = request.user
    channel_layer = get_channel_layer()
    data = "notification"+ "...." + str(datetime.now())
    # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
        str(current_user.pk),  # Channel Name, Should always be string
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": data,
        },
    )  
    return render(request, 'django_notifications_app/notifications_test_page.html')

'''
