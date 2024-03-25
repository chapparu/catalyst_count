from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/',views.menupage, name='menupage'),
    path('upload/',views.uploadpage, name='uploadpage'),
    path('user/',views.userpage, name='userpage'),
    path('builder/',views.builderpage, name='builderpage'),
    path('add/', views.add_user, name='add_user'),
    path('delete/<id>/', views.delete_user, name='delete_user'),
    path('add_query/',views.add_query, name='add_query'),
]