from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from reviews.models import Review


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
