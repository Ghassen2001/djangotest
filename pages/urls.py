from django.urls import path
from .views import homePageView, index , listBooks, show, add, edit, remove


app_name = 'pages'

urlpatterns = [
    path('', homePageView, name="home"),
    path('index/', index, name="index"),
    path('books/', listBooks, name='listBooks'),
    path('<int:book_id>/', show,name='show'),
    path('ajouter_livre/', add,name='add'),
    path('supprimer_livre/', remove, name='remove'),
    path('modifier_livre/', edit,name='edit'),


]