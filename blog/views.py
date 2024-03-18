from django.shortcuts import render
from .models import City, Category, Tag
from .serializers import CategorySerializer, TagSerializer, CitySerializer
from rest_framework import generics


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        if tag:
            return City.objects.filter(tags__title__icontains=tag)
        if category:
            return City.objects.filter(category__title__icontains=category)
        else:
            return City.objects.all()