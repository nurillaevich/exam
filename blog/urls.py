from django.urls import path
from .views import TagList, CityList, CategoryList
urlpatterns = [
    path('', CityList.as_view(), name='city'),
    path('tags/', TagList.as_view(), name='tag'),
    path('category/', CategoryList.as_view(), name='category')
]
