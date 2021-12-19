from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Manga, Chapter
from django.views.generic import ListView
from django.contrib.auth.models import User
from user.models import Favorit, List, ListItem
from django.core.paginator import Paginator
# Create your views here.

def index(request):
	manga = Manga.objects.order_by('-rate').all()
	manga = manga[0:15]
	latest_chapter = Chapter.objects.order_by('-pub_date').all()
	latest_chapter = latest_chapter[:9]
	context = {
		'manga':manga,
		'chapter': latest_chapter,
		'tab':'home',
		}
	return render(request,'anime/index.html', context)

def manga(request, manga_name):
	manga = get_object_or_404(Manga, name=manga_name)
	#manga = Manga.objects.get(name=manga_name)
	user = request.user
	fav_manga = user.favorit_set.values_list('manga',flat=True)
	lists = user.list_set.all()
	in_fav = True if manga.id in fav_manga else False

	lista = user.list_set.all()[0]
	manga_in_the_list = lista.listitem_set.values_list('manga',flat=True) 
	in_list = True if manga.id in manga_in_the_list else False

	listitems = []
	listas = user.list_set.all()
	for l in listas:
		manga_in_the_list = list(l.listitem_set.values_list('manga',flat=True))
		listitems.append(manga_in_the_list)

	chapters = None
	try:
		chapters = manga.chapter_set.all()
	except Exception as e:
		print(e)
	context = {
		'manga':manga,
		'chapters': chapters,
		'in_fav': in_fav,
		'lists':lists,
		'listitems':listitems,
		'in_list': in_list,
		'tab':'manga',
		}
	return render(request, 'anime/manga.html', context)

class MangaListView(ListView):
	model = Manga
	order_by = '-rate'
	template_name = 'anime/all_manga.html'
	paginate_by = 15
	# get_context_object_name = modelName_list by default

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tab'] = 'manga'
		return context






'''
class MangaListView(ListView):
	model = Manga
	template_name = 'anime/index.html'
	context_object_name = 'manga'
	paginate_by = 9

'''


def add_to_fav(request):
	if request.is_ajax and request.method == "POST":
		try:
			manga_id = request.POST.get('manga_id')
			manga = Manga.objects.get(pk=manga_id)
			user = request.user

			fav_manga = Favorit(user=user, manga=manga)
			fav_manga.save()
			data = {
				'manga_name':'manga.name'
			}


			return JsonResponse(data, status=200)
		except Exception as e:
			print("crap2")
			return JsonResponse({"error":"str(e)"}, status=404)

def remove_from_fav(request):
	if request.is_ajax and request.method == "POST":
		try:
			manga_id = request.POST.get('manga_id')
			manga = Manga.objects.get(pk=manga_id)
			user = request.user

			fav_manga = Favorit.objects.filter(user=user, manga=manga)
			fav_manga[0].delete()
			data = {
				'manga_name':'manga.name'
			}


			return JsonResponse(data, status=200)
		except Exception as e:
			print("crap2")
			return JsonResponse({"error":str(e)}, status=404)

def add_to_list(request):
	if request.is_ajax and request.method == "POST":
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
				'manga_name':'manga.name',
				'list_js': None,
			}
			return JsonResponse(data, status=200)
		except Exception as e:
			print("crap2")
			return JsonResponse({"error":str(e)}, status=404)
'''
'''
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
				'manga_name':'manga.name'
			}


			return JsonResponse(data, status=200)
		except Exception as e:
			print("crap2")
			return JsonResponse({"error":str(e)}, status=404)

def add_new_list(request):
	if request.is_ajax and request.method == "POST":
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

			return JsonResponse({"new_list":new_list}, status=200)
		except Exception as e:
			print("crap2")
			return JsonResponse({"error":str(e)}, status=404)


def Lists(request):
	user = request.user
	
	lists_ = user.list_set.all()
	paginator = Paginator(lists_, 5) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	print(lists_)
	context = {

		'tab':'lists',
		'page_obj':page_obj,
		}
	return render(request, 'anime/lists.html', context)

def ListDetails(request, list_name):
	user = request.user
	lista = List.objects.get(user=user, name=list_name)
	list_items = lista.listitem_set.all()

	paginator = Paginator(list_items, 15) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
	
		'tab':'lists',
		'page_obj':page_obj,
		}
	return render(request, 'anime/list.html', context)

def Favlist(request):
	user = request.user
	fav_items = user.favorit_set.all()

	paginator = Paginator(fav_items, 15) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
	
		'tab':'fav',
		'page_obj':page_obj,
		}
	return render(request, 'anime/list.html', context)

