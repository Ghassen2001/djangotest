from django.urls import path
from .views import homePageView, index

urlpatterns = [
    path('', homePageView, name="home"),
    path('index/', index, name="index"),
]