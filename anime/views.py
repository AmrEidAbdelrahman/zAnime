from django.shortcuts import render
from .models import Manga
# Create your views here.

def index(request):
	manga = Manga.objects.order_by('-rate').all()
	manga = manga[0:9]
	context = {
		'manga':manga,
		'tab':'home',
		}
	return render(request,'anime/index.html', context)

'''
class MangaListView(ListView):
	model = Manga
	template_name = 'anime/index.html'
	context_object_name = 'manga'
	paginate_by = 9

'''