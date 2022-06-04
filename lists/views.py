from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .models import List


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
        return render(request, 'lists/lists.html', context)

    def retrieve(self, request, *args, **kwargs):
        print("retrieve")
        instance = get_object_or_404(List, name=kwargs['name'])
        print(instance.listitem_set.all())
        context = {
            'list': instance,
            'tab': 'lists',
        }
        return render(request, 'lists/list.html', context)