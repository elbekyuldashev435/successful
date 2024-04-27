from django.urls import path
from .views import home_page, news


urlpatterns = [
    path('', home_page, name='home-page'),
    path('news/', news, name='daily-news'),
]