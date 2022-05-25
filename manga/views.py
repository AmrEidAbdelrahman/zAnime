from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet


class MangaView(ModelViewSet):

    def list(self, request, *args, **kwargs):
        return render(request, 'manga/index.html')

    def retrieve(self, request, *args, **kwargs):
        return render(request, 'manga/details.html')
