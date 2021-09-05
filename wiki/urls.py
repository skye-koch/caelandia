from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:pk>', views.wikipage, name = "wikipage"),
    path('new', views.createEntry, name = 'createEntry' ),
    path('update/<int:pk>', views.updateEntry, name = 'updateEntry'), 
    path('delete/<int:pk>', views.deleteEntry, name = 'deleteEntry'),
    path('search', views.search, name = 'search'),
    path('category/<str:catName>', views.catpage, name = 'category'),
]