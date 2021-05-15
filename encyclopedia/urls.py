from encyclopedia import search
from django.urls import path, re_path
from . import views
app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("test/",views.entryview, name="test"),
    path("<str:TITLE>",views.entryview, name='title'),
    path("search/",views.searchform, name = 'search'),
    path("newpage/",views.add, name='add'),
    path("edit/<str:abs>", views.edit, name='edit'),
    path("random/", views.random, name='random')

]
