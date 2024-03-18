from rest_framework import serializers
from .models import City, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']


class CitySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer()

    class Meta:
        model = City
        fields = ['country', 'image', 'category', 'tags']
