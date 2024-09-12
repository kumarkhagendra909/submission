# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
    path('', views.comments_list, name='comments_list'),
]
